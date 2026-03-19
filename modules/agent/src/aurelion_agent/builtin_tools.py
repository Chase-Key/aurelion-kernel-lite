"""
aurelion_agent.builtin_tools — Ready-made @tool functions for common agent needs.

Import the ones you want and pass them to your agent:

    from aurelion_agent.builtin_tools import web_search, get_current_time
    agent = MyAgent("Demo", llm=llm, tools=[web_search, get_current_time])

Available tools:
    web_search(query)         — DuckDuckGo search, returns top results (no API key)
    get_current_time()        — Current UTC date and time
    calculate(expression)     — Safe arithmetic evaluation
"""

from __future__ import annotations

from .tools import tool


@tool(description="Search the web using DuckDuckGo and return the top results. Use this to look up current events, factual information, documentation, or anything you don't know from memory.")
def web_search(query: str, num_results: int = 5) -> str:
    """
    Search DuckDuckGo and return a formatted list of results.

    Args:
        query: The search query.
        num_results: How many results to return (1-10). Default 5.

    Returns:
        Formatted string of results with title, URL, and snippet.
    """
    try:
        from ddgs import DDGS
    except ImportError:
        try:
            from duckduckgo_search import DDGS
        except ImportError:
            return (
                "web_search is unavailable — install ddgs:\n"
                "  pip install ddgs"
            )

    num_results = max(1, min(num_results, 10))
    results = []

    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=num_results):
                title   = r.get("title", "")
                href    = r.get("href", "")
                body    = r.get("body", "")
                results.append(f"**{title}**\n{href}\n{body}")
    except Exception as exc:
        return f"Search failed: {exc}"

    if not results:
        return f"No results found for: {query}"

    return f"Search results for '{query}':\n\n" + "\n\n---\n\n".join(results)


@tool(description="Get the current UTC date and time. Use this when the user asks what time or date it is.")
def get_current_time() -> str:
    """Returns the current UTC date and time as a readable string."""
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc)
    return now.strftime("Current time: %A, %B %d, %Y at %H:%M UTC")


@tool(description="Evaluate a safe arithmetic expression and return the result. Use for calculations involving +, -, *, /, **, and parentheses.")
def calculate(expression: str) -> str:
    """
    Safely evaluate a math expression.

    Args:
        expression: A math expression string, e.g. '(12 * 4) / 3 + 2**8'

    Returns:
        The numeric result as a string, or an error message.
    """
    import ast
    import operator

    _SAFE_OPS = {
        ast.Add:  operator.add,
        ast.Sub:  operator.sub,
        ast.Mult: operator.mul,
        ast.Div:  operator.truediv,
        ast.Pow:  operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    def _eval(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        elif isinstance(node, ast.BinOp):
            op = _SAFE_OPS.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported operator: {node.op}")
            return op(_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp):
            op = _SAFE_OPS.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported operator: {node.op}")
            return op(_eval(node.operand))
        else:
            raise ValueError(f"Unsupported expression type: {type(node)}")

    try:
        tree = ast.parse(expression.strip(), mode="eval")
        result = _eval(tree.body)
        return f"{expression} = {result}"
    except Exception as exc:
        return f"Could not evaluate '{expression}': {exc}"
