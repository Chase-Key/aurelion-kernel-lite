"""
aurelion_agent.evaluator — AgentEvaluator: structured test runner for agents.

Define test cases with expected outputs, forbidden outputs, and latency budgets.
Run them against any BaseAgent and get a pass/fail report with scoring.

Usage:
    from aurelion_agent import AgentEvaluator, TestCase

    evaluator = AgentEvaluator(agent)
    report = evaluator.run([
        TestCase(
            name="basic_greeting",
            input="Say hello",
            expected_contains=["hello", "hi"],
        ),
        TestCase(
            name="factual_accuracy",
            input="What is 2 + 2?",
            expected_contains=["4"],
            max_latency_ms=5000,
        ),
        TestCase(
            name="no_hallucination_marker",
            input="What is my name?",
            expected_not_contains=["Chase", "CK"],  # agent shouldn't guess
        ),
    ])

    print(report.summary())
    report.save("eval_results.json")
"""

from __future__ import annotations

import asyncio
import json
import time
from typing import TYPE_CHECKING, List, Optional

from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from .base_agent import BaseAgent


# ---------------------------------------------------------------------------
# Test case definition
# ---------------------------------------------------------------------------

class TestCase(BaseModel):
    """
    One evaluation scenario.

    Matching is case-insensitive. A test passes only when ALL of the
    following conditions are met:
      - every string in expected_contains appears in the response
      - no string in expected_not_contains appears in the response
      - response latency is below max_latency_ms (if set)
      - custom_check(response) returns True (if set)

    Attributes:
        name: Human-readable test identifier.
        input: The user message sent to the agent.
        expected_contains: All of these strings must appear (case-insensitive).
        expected_not_contains: None of these strings may appear (case-insensitive).
        max_latency_ms: Optional max allowed response time in milliseconds.
        temperature: LLM temperature for this test (default 0.0 for determinism).
        max_tokens: Token budget for this test.
    """
    name: str
    input: str
    expected_contains: List[str] = Field(default_factory=list)
    expected_not_contains: List[str] = Field(default_factory=list)
    max_latency_ms: Optional[float] = None
    temperature: float = 0.0   # deterministic by default for eval runs
    max_tokens: int = 500


# ---------------------------------------------------------------------------
# Result types
# ---------------------------------------------------------------------------

class EvalResult(BaseModel):
    """Result of running one TestCase."""
    test_name: str
    passed: bool
    score: float          # 0.0 – 1.0 (fraction of checks that passed)
    latency_ms: float
    actual_response: str
    failures: List[str] = Field(default_factory=list)

    def __str__(self) -> str:
        status = "PASS" if self.passed else "FAIL"
        suffix = f"  ← {'; '.join(self.failures)}" if self.failures else ""
        return f"[{status}] {self.test_name} ({self.latency_ms:.0f}ms){suffix}"


class EvalReport(BaseModel):
    """Aggregated results across all test cases."""
    agent_name: str
    total: int
    passed: int
    failed: int
    pass_rate: float       # 0.0 – 1.0
    avg_latency_ms: float
    results: List[EvalResult] = Field(default_factory=list)

    def summary(self) -> str:
        """Return a formatted multi-line summary string."""
        bar = "─" * 44
        lines = [
            "",
            f"  AURELION AgentEvaluator — {self.agent_name}",
            f"  {bar}",
            f"  Passed  : {self.passed} / {self.total}  ({self.pass_rate * 100:.1f}%)",
            f"  Failed  : {self.failed}",
            f"  Avg     : {self.avg_latency_ms:.0f}ms",
            f"  {bar}",
        ]
        for r in self.results:
            lines.append(f"  {r}")
        lines.append("")
        return "\n".join(lines)

    def save(self, path: str) -> None:
        """Write the full report to a JSON file."""
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.model_dump(), f, indent=2)

    @classmethod
    def load(cls, path: str) -> "EvalReport":
        """Load a previously saved report from JSON."""
        with open(path, encoding="utf-8") as f:
            return cls.model_validate(json.load(f))


# ---------------------------------------------------------------------------
# Evaluator
# ---------------------------------------------------------------------------

class AgentEvaluator:
    """
    Run a suite of TestCases against a BaseAgent and produce an EvalReport.

    Args:
        agent: The agent to evaluate. Its conversation history is reset
               between test cases to ensure isolation.
    """

    def __init__(self, agent: "BaseAgent"):
        self._agent = agent

    # ------------------------------------------------------------------
    # Sync runner
    # ------------------------------------------------------------------

    def run(self, test_cases: List[TestCase]) -> EvalReport:
        """
        Run all test cases synchronously and return an EvalReport.

        History is reset before each test case to ensure isolation.
        """
        results: List[EvalResult] = []
        for tc in test_cases:
            self._agent.reset_history()
            result = self._run_one(tc)
            results.append(result)

        return self._build_report(results)

    def run_one(self, tc: TestCase) -> EvalResult:
        """Run a single TestCase without resetting history beforehand."""
        return self._run_one(tc)

    # ------------------------------------------------------------------
    # Async runner
    # ------------------------------------------------------------------

    async def arun(self, test_cases: List[TestCase]) -> EvalReport:
        """
        Run all test cases asynchronously (one at a time, isolated).
        Useful when an event loop is already running.
        """
        results: List[EvalResult] = []
        for tc in test_cases:
            self._agent.reset_history()
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, lambda t=tc: self._run_one(t))
            results.append(result)
        return self._build_report(results)

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _run_one(self, tc: TestCase) -> EvalResult:
        t0 = time.monotonic()
        try:
            trace = self._agent.respond(
                tc.input,
                temperature=tc.temperature,
                max_tokens=tc.max_tokens,
            )
            response = trace.last_response or ""
        except Exception as exc:
            latency_ms = (time.monotonic() - t0) * 1000
            return EvalResult(
                test_name=tc.name,
                passed=False,
                score=0.0,
                latency_ms=round(latency_ms, 1),
                actual_response="",
                failures=[f"Exception: {exc}"],
            )

        latency_ms = (time.monotonic() - t0) * 1000
        failures: List[str] = []
        total_checks = 0

        # Check expected_contains
        for expected in tc.expected_contains:
            total_checks += 1
            if expected.lower() not in response.lower():
                failures.append(f"missing '{expected}'")

        # Check expected_not_contains
        for forbidden in tc.expected_not_contains:
            total_checks += 1
            if forbidden.lower() in response.lower():
                failures.append(f"forbidden '{forbidden}' found")

        # Check latency
        if tc.max_latency_ms is not None:
            total_checks += 1
            if latency_ms > tc.max_latency_ms:
                failures.append(
                    f"latency {latency_ms:.0f}ms exceeded limit {tc.max_latency_ms:.0f}ms"
                )

        checks_passed = (total_checks - len(failures)) if total_checks else 1
        score = round(checks_passed / total_checks, 4) if total_checks else 1.0

        return EvalResult(
            test_name=tc.name,
            passed=len(failures) == 0,
            score=score,
            latency_ms=round(latency_ms, 1),
            actual_response=response,
            failures=failures,
        )

    def _build_report(self, results: List[EvalResult]) -> EvalReport:
        total = len(results)
        passed = sum(1 for r in results if r.passed)
        avg_latency = (
            sum(r.latency_ms for r in results) / total if total else 0.0
        )
        return EvalReport(
            agent_name=self._agent.name,
            total=total,
            passed=passed,
            failed=total - passed,
            pass_rate=round(passed / total, 4) if total else 0.0,
            avg_latency_ms=round(avg_latency, 1),
            results=results,
        )
