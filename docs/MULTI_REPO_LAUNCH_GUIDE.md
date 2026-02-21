# Phase 1 Multi-Repo Launch Guide

**How to push 6 independent repos from your aurelion-eco workspace**

**Time:** 30-45 minutes total  
**Result:** 6 public GitHub repos (5 modules + 1 hub)

---

## Overview

You have one local workspace (`aurelion-eco`). You'll push 6 subdirectories as separate GitHub repos:

1. `aurelion-kernel-lite`
2. `aurelion-memory-lite`
3. `aurelion-advisor-lite`
4. `aurelion-agent-lite`
5. `aurelion-nexus-lite`
6. `aurelion-hub`

**Each repo is independent.** Users can clone one, some, or all.

---

## Pre-Launch: Update Module READMEs

Each module needs a "Related Modules" section linking to other repos.

**Skip this step for now** - we'll add after repos exist (otherwise links break).

---

## Step 1: Create 6 GitHub Repositories (10 min)

Go to: https://github.com/new

### Repo 1: aurelion-kernel-lite

- **Name:** `aurelion-kernel-lite`
- **Description:** `5-floor cognitive structure templates for organizing complex thinking`
- **Visibility:** ✅ Public
- **Initialize:** ❌ Do NOT check any boxes
- Click **Create repository**
- **Copy URL:** `https://github.com/chase-key/aurelion-kernel-lite.git`

### Repo 2: aurelion-memory-lite

- **Name:** `aurelion-memory-lite`
- **Description:** `File-based knowledge graph for persistent personal memory`
- **Visibility:** ✅ Public
- **Initialize:** ❌ Do NOT check any boxes
- Click **Create repository**
- **Copy URL:** `https://github.com/chase-key/aurelion-memory-lite.git`

### Repo 3: aurelion-advisor-lite

- **Name:** `aurelion-advisor-lite`
- **Description:** `Career planning templates and strategic methodology library`
- **Visibility:** ✅ Public
- **Initialize:** ❌ Do NOT check any boxes
- Click **Create repository**
- **Copy URL:** `https://github.com/chase-key/aurelion-advisor-lite.git`

### Repo 4: aurelion-agent-lite

- **Name:** `aurelion-agent-lite`
- **Description:** `100+ AI collaboration prompts and strategic thinking protocols`
- **Visibility:** ✅ Public
- **Initialize:** ❌ Do NOT check any boxes
- Click **Create repository**
- **Copy URL:** `https://github.com/chase-key/aurelion-agent-lite.git`

### Repo 5: aurelion-nexus-lite

- **Name:** `aurelion-nexus-lite`
- **Description:** `Story-agnostic simulation framework for NPCs, locations, and world-building`
- **Visibility:** ✅ Public
- **Initialize:** ❌ Do NOT check any boxes
- Click **Create repository**
- **Copy URL:** `https://github.com/chase-key/aurelion-nexus-lite.git`

### Repo 6: aurelion-hub

- **Name:** `aurelion-hub`
- **Description:** `Central documentation hub for the AURELION modular cognitive architecture`
- **Visibility:** ✅ Public
- **Initialize:** ❌ Do NOT check any boxes
- Click **Create repository**
- **Copy URL:** `https://github.com/chase-key/aurelion-hub.git`

---

## Step 2: Push Each Module (25 min total, ~4 min each)

**Run these commands for each module:**

### Module 1: KERNEL-Lite

```powershell
cd "c:\Users\chase\.vscode\Personal Projects\aurelion-eco\modules\kernel\aurelion-kernel-lite"

# Initialize git
git init

# Stage all files
git add .

# VERIFY: Make sure you're in the right directory
pwd  # Should show: .../aurelion-kernel-lite

# Commit
git commit -m "Phase 1: KERNEL-Lite v1.0.0

5-floor cognitive structure templates:
- Floor 01: Foundation (data, facts, raw material)
- Floor 02: Systems (patterns, connections, rules)
- Floor 03: Networks (relationships, ecosystem)
- Floor 04: Action (goals, plans, execution)
- Floor 05: Vision (purpose, meaning, direction)

8 production-ready templates included."

# Connect to GitHub (replace chase-key)
git remote add origin https://github.com/chase-key/aurelion-kernel-lite.git

# Set branch to main
git branch -M main

# Push
git push -u origin main
```

**Expected output:** `Writing objects: 100%...` then success message.

---

### Module 2: MEMORY-Lite

```powershell
cd "c:\Users\chase\.vscode\Personal Projects\aurelion-eco\modules\memory\aurelion-memory-lite"

git init
git add .

git commit -m "Phase 1: MEMORY-Lite v1.0.0

File-based knowledge graph with Python API:
- JSON storage (no database required)
- Node and edge relationships
- Query API for retrieval
- Persistent personal memory system

Production-ready for individual use."

git remote add origin https://github.com/chase-key/aurelion-memory-lite.git
git branch -M main
git push -u origin main
```

---

### Module 3: ADVISOR-Lite

```powershell
cd "c:\Users\chase\.vscode\Personal Projects\aurelion-eco\modules\advisor\aurelion-advisor-lite"

git init
git add .

git commit -m "Phase 1: ADVISOR-Lite v0.2.0

Career planning and strategic methodology library:
- 12 planning templates
- Alex Thompson case study (6 examples)
- Investigation methodologies
- Decision frameworks

Beta release for strategic planning use cases."

git remote add origin https://github.com/chase-key/aurelion-advisor-lite.git
git branch -M main
git push -u origin main
```

---

### Module 4: AGENT-Lite

```powershell
cd "c:\Users\chase\.vscode\Personal Projects\aurelion-eco\modules\agent\aurelion-agent-lite"

git init
git add .

git commit -m "Phase 1: AGENT-Lite v0.2.0

AI collaboration prompts and protocols:
- 100 curated prompt patterns (46 detailed + 54 indexed)
- Strategic Advisor Protocol
- Session Management Guide
- Context-building techniques

Beta release for AI-assisted workflows."

git remote add origin https://github.com/chase-key/aurelion-agent-lite.git
git branch -M main
git push -u origin main
```

---

### Module 5: NEXUS-Lite

```powershell
cd "c:\Users\chase\.vscode\Personal Projects\aurelion-eco\modules\nexus\aurelion-nexus-lite"

git init
git add .

git commit -m "Phase 1: NEXUS-Lite v0.1.0

Story-agnostic simulation framework:
- NPCs with personality and memory
- Locations and events
- World state tracking
- Python-based, no AI dependencies

Beta release for simulation and world-building."

git remote add origin https://github.com/chase-key/aurelion-nexus-lite.git
git branch -M main
git push -u origin main
```

---

### Module 6: HUB

```powershell
cd "c:\Users\chase\.vscode\Personal Projects\aurelion-eco\aurelion-hub"

git init
git add .

git commit -m "Phase 1: AURELION Hub Launch

Central documentation for AURELION Ecosystem:
- Module overview and comparison
- Getting started guide
- Integration guides (KERNEL+MEMORY, ADVISOR+AGENT)
- CK's journey: how the system was built
- Philosophy: why modular cognitive architecture

Links to all 5 module repositories."

git remote add origin https://github.com/chase-key/aurelion-hub.git
git branch -M main
git push -u origin main
```

---

## Step 3: Verify on GitHub (5 min)

**For each repository, check:**

### KERNEL, MEMORY, ADVISOR, AGENT, NEXUS
- ✅ Files visible (Floor directories, Python files, templates)
- ✅ README displays correctly
- ✅ LICENSE file present (MIT)
- ❌ No premium module content
- ❌ No `.env` files or API keys

### HUB
- ✅ README displays with module links
- ✅ Docs folder with guides
- ✅ Links work (after Step 4)

---

## Step 4: Update Module READMEs with Cross-Links (5 min)

Now that repos exist, **add "Related Modules" section to each README**.

### Template for Each Module

Add this near the end of each module's README:

```markdown
## 🔗 Related Modules

AURELION is modular. This module works great standalone or combined with:

- **[MEMORY-Lite](https://github.com/chase-key/aurelion-memory-lite)** - Store your structures persistently
- **[ADVISOR-Lite](https://github.com/chase-key/aurelion-advisor-lite)** - Strategic planning templates
- **[AGENT-Lite](https://github.com/chase-key/aurelion-agent-lite)** - AI collaboration prompts
- **[NEXUS-Lite](https://github.com/chase-key/aurelion-nexus-lite)** - Simulation framework

→ **[AURELION Hub](https://github.com/chase-key/aurelion-hub)** - Integration guides and ecosystem overview

**Start with one module. Add more as you need them.**
```

Update each module's README locally, then:

```powershell
# Navigate to module
cd "c:\Users\chase\.vscode\Personal Projects\aurelion-eco\modules\kernel\aurelion-kernel-lite"

# Stage, commit, push
git add README.md
git commit -m "Add Related Modules section with cross-links"
git push
```

Repeat for all 5 modules.

---

## Step 5: Configure Repository Settings (5 min each)

For **each repository**, go to Settings:

### Topics (Discoverability)

**KERNEL:** `cognitive-architecture`, `templates`, `thinking-tools`, `knowledge-management`

**MEMORY:** `knowledge-graph`, `personal-memory`, `file-based`, `python`

**ADVISOR:** `career-planning`, `strategic-planning`, `templates`, `methodology`

**AGENT:** `ai-prompts`, `ai-collaboration`, `chatgpt`, `claude`, `prompt-engineering`

**NEXUS:** `simulation`, `world-building`, `npc`, `game-master`, `storytelling`

**HUB:** `documentation`, `cognitive-architecture`, `modular-framework`, `aurelion`

### About Section

- Add description (use the ones from Step 1)
- Enable ✅ Releases
- Enable ✅ Packages (for future)

---

## GitHub Authentication (If Needed)

**If any `git push` asks for password:**

### Get Personal Access Token

1. Go to: https://github.com/settings/tokens
2. **Generate new token (classic)**
3. **Note:** `aurelion-modules`
4. **Expiration:** 90 days
5. Check ✅ **repo**
6. Click **Generate token**
7. **Copy immediately** (looks like `ghp_ABC123...`)

### Use Token

```
Username: YOUR-GITHUB-USERNAME
Password: [paste token here]
```

### Remember It

```powershell
git config --global credential.helper wincred
```

Windows will save it.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Not a git repository" | Make sure you're in module directory, not parent |
| "Remote already exists" | `git remote remove origin` then add again |
| "Permission denied" | Use HTTPS URL, not SSH |
| Wrong directory pushed | Check with `pwd` before `git init` |

---

## Post-Launch Verification Checklist

- [ ] 6 repos created on GitHub
- [ ] All 5 modules pushed successfully
- [ ] Hub pushed successfully
- [ ] Each module README has "Related Modules" section
- [ ] Hub links to all 5 modules
- [ ] No premium content visible anywhere
- [ ] No API keys or secrets visible
- [ ] Topics added to each repo
- [ ] Descriptions set for each repo

---

## Future Updates

**When you update a module locally:**

```powershell
# Navigate to module
cd "c:\Users\chase\.vscode\Personal Projects\aurelion-eco\modules\kernel\aurelion-kernel-lite"

# Make changes...

# Stage and push
git add .
git commit -m "Your update message"
git push
```

**Each module updates independently** - no need to update others.

---

## Phase 2: Premium Modules (Q3 2026)

When ready to launch premium tiers:

1. Sanitize premium modules (remove API keys)
2. Create new repos for each premium module
3. Push the same way as Lite modules
4. Update Hub to link to premium repos

**Keep nexus-premium private forever** (has production deployment keys).

---

## Summary

**What users see:**
- 6 independent repos
- Each cloneable separately
- Hub explains how they connect

**What you maintain:**
- One `aurelion-eco` workspace locally
- Push subdirectories as separate repos
- Each module updates independently

**Philosophy:**
Users build their own AURELION by choosing modules that fit their needs.

---

**Time:** 30-45 minutes  
**Result:** 🚀 Phase 1 launched - 5 Lite modules + Hub live on GitHub!

