# AURELION → Agent Skills Distribution Strategy
**Date:** February 21, 2026  
**Author:** CK (chase-key)  
**Context:** Post-launch feedback from Lead AI Engineer at LexisNexis  
**Status:** Active Implementation Plan

---

## The Situation

Four lite modules launched Feb 17, 2026 on github.com/chase-key:
- `aurelion-kernel-lite` — 5-floor cognitive kernel templates
- `aurelion-memory-lite` — File-based knowledge graph + Python API
- `aurelion-advisor-lite` — Strategic planning & career methodology frameworks
- `aurelion-agent-lite` — AI collaboration protocols and critical thinking prompts

Expert feedback: **Distribution is the bottleneck, not capability.**

The Anthropic Agent Skills ecosystem and Vercel marketplace (`skills.vercel.ai`) offer a direct path to 100k+ developer eyeballs with minimal restructuring.

---

## Honest Assessment: What's Sharp and What's Overstated

### What the feedback gets exactly right

**"Your modules are basically skills already."**  
This is accurate. KERNEL templates, ADVISOR frameworks, and AGENT prompts are pure instruction-sets. They don't need a runtime. Restructuring each into a `SKILL.md` + `skill-manifest.json` is a 1–4 hour lift per module — not a refactor.

**"MEMORY could work as an MCP server."**  
Correct. `aurelion-memory-lite` already has a Python API and file-based storage with no external dependencies. An MCP (Model Context Protocol) server wrapper exposes it to Claude Desktop, VS Code Copilot Chat, and any MCP-compatible client with a single config entry.

**"One command install → way more eyeballs."**  
Accurate. The Skills marketplace is the npm for agents right now. Top skills at 100k+ installs are mostly thin instruction wrappers. AURELION's quality is above that baseline.

### Where to apply skepticism

**Don't dissolve the GitHub org structure.**  
Skills are a *distribution layer*, not a replacement architecture. Push Skills to `skills.vercel.ai`, maintain the full ecosystem at `github.com/chase-key`. These work together. Vercel marketplace drives discovery → GitHub is the full product.

**Skills are ephemeral; the ecosystem creates moat.**  
Any developer can publish a "thinking template skill." What they can't replicate is a unified cross-module ecosystem with a clear philosophy (Darklight Chambers, AAI architecture, markdown-first). Protect the brand — the `AURELION` name should be prominent in every Skill listing.

**"Premium/enterprise roadmap" is not dead.**  
Skills expand your audience, which *accelerates* premium conversion. The two paths reinforce each other. Don't abandon the tiering strategy.

---

## Implementation Plan

### Phase 1 — Skills Layer (This Week)
Add `SKILL.md` + `skill-manifest.json` to each lite module.  
No code changes. Ship to Vercel marketplace.

| Module | Skill Name | Category |
|--------|-----------|----------|
| kernel-lite | AURELION Kernel — Structured Thinking | Productivity, Knowledge Management |
| advisor-lite | AURELION Advisor — Career Strategy | Career, Planning |
| agent-lite | AURELION Agent — AI Collaboration Protocols | AI, Productivity |
| memory-lite | (MCP server — separate path) | Tools |

**Files needed per skill module:**
```
{module}/
  SKILL.md            ← Natural language instructions for the agent runtime
  skill-manifest.json ← Metadata: name, version, author, categories, entrypoint
```

### Phase 2 — Memory as MCP Server (1–2 Weeks)
Wrap `aurelion_memory_lite` Python package in a proper MCP server.

**Files needed:**
```
modules/memory/aurelion-memory-lite/
  mcp/
    server.py          ← MCP server entry point (FastMCP or raw JSON-RPC)
    README.md          ← One-command install instructions
    requirements.txt   ← mcp, fastmcp (or raw stdlib only)
```

**MCP install entry for users:**
```json
{
  "mcpServers": {
    "aurelion-memory": {
      "command": "python",
      "args": ["-m", "aurelion_memory_mcp"],
      "env": { "AURELION_PATH": "/path/to/your/memory-store" }
    }
  }
}
```

### Phase 3 — Simple Installer (2–4 Weeks)
A single shell script or `npx` command that installs all four modules.

```bash
# Option A — Shell (works cross-platform)
curl -sSL https://aurelion.dev/install | sh

# Option B — npx (if you add a thin Node wrapper)
npx aurelion install

# Option C — pip (since memory already has setup.py)
pip install aurelion-stack
```

Recommendation: **start with the shell script**. You already have a Python setup.py in memory-lite. Extend it first, then add npx later when there's demand for it. Don't over-engineer phase 3 until phases 1 and 2 prove traction.

### Phase 4 — Skills.vercel.ai Submission
Once SKILL.md files are live in the repos:
1. Create account at `skills.vercel.ai`
2. Submit each skill via the marketplace form (links to GitHub repo)
3. Tag with `aurelion` across all four submissions so they cross-link
4. Monitor install counts — use this data to prioritize premium roadmap

---

## Technical Specs: SKILL.md Format

Anthropic's Agent Skills spec (`github.com/anthropics/skills`) defines a SKILL.md as:
- **YAML frontmatter** — machine-readable metadata
- **Markdown body** — natural language instructions that the AI agent reads directly
- Compatible with: Claude Code, Codex CLI, ChatGPT (via the open spec)

Critical rule: **the body of SKILL.md is read by the AI, not by a developer.** Write it as instructions to an agent, not documentation for a human. This is the most common mistake when converting existing READMEs to Skills.

---

## Known Issues

✅ ~~`modules/memory/aurelion-memory-lite/README.md` had an unresolved git merge conflict (resolved Feb 21, 2026 — all 5 conflict regions removed, Memory content preserved)~~

---

## Files Created This Session

| File | Purpose |
|------|---------|
| `docs/planning/skills-strategy.md` | This document — master strategy |
| `modules/kernel/aurelion-kernel-lite/SKILL.md` | Kernel skill instructions |
| `modules/kernel/aurelion-kernel-lite/skill-manifest.json` | Kernel skill metadata |
| `modules/advisor/aurelion-advisor-lite/SKILL.md` | Advisor skill instructions |
| `modules/advisor/aurelion-advisor-lite/skill-manifest.json` | Advisor skill metadata |
| `modules/agent/aurelion-agent-lite/SKILL.md` | Agent skill instructions |
| `modules/agent/aurelion-agent-lite/skill-manifest.json` | Agent skill metadata |
| `modules/memory/aurelion-memory-lite/SKILL.md` | Memory skill (overview + MCP pointer) |
| `modules/memory/aurelion-memory-lite/skill-manifest.json` | Memory skill metadata |
| `modules/memory/aurelion-memory-lite/mcp/server.py` | MCP server entry point |
| `modules/memory/aurelion-memory-lite/mcp/README.md` | MCP install instructions |
| `docs/email-reply-draft.md` | Email reply to LexisNexis engineer |

---

## Success Metrics

Track these monthly after Skills launch:
- Vercel marketplace install counts per skill
- GitHub stars delta (before/after Skills listing)
- Issues and PRs from net-new contributors (currently zero)
- First external fork date

The goal for 90 days post-launch: **500+ total skill installs across all four modules.** If any single skill hits 1k installs, prioritize the premium conversion path for that module first.
