# AURELION Module Modification Specifications
**Date:** February 16, 2026  
**Purpose:** Detailed changes required for each module based on FTO analysis  
**Priority:** Complete before Q2 2026 public launch  
**Status:** ✅ Critical naming issues resolved (February 16, 2026)

---

## ✅ COMPLETED MODIFICATIONS (February 16, 2026)

### 1. AAI Naming Resolution ✅
- **Issue:** AAAI trademark conflict
- **Solution:** AAAI → AAI (40 files updated)
- **Status:** Complete

### 2. ADVISOR Module Naming ✅  
- **Issue:** COMPASS generic naming
- **Solution:** COMPASS → ADVISOR (38 files + 4 directories)
- **Status:** Complete

### 3. PATENT_NOTICE Files ✅
- All 5 MIT-licensed modules updated
- Status: Complete

---

## 🎯 Quick Reference: Risk Levels by Module

| Module | Patent Risk | Trademark Risk | Changes Required | Priority |
|--------|-------------|----------------|------------------|----------|
| **Kernel** | Very Low | Low | Minimal | LOW |
| **Memory** | Medium | Low | Moderate | MEDIUM |
| **Advisor** | Low | Medium-High | Moderate | HIGH |
| **Agent** | Medium-High | Low | Significant | HIGH |
| **Nexus** | High | Low | Significant | CRITICAL |
| **AAI-Complete** | Medium | Very High | Major (rename) | CRITICAL |

---

## 📦 MODULE 1: aurelion-kernel-lite

### Current Status
✅ Already safe - templates are not patentable  
✅ Naming is fine: `aurelion-kernel-lite`

### Required Changes

#### 1. Add PATENT_NOTICE File
**File:** `modules/kernel/aurelion-kernel-lite/PATENT_NOTICE`

```
PATENT NOTICE

This project is licensed under the MIT License.

No patent rights are granted, whether express or implied. Use of this software
may require patent licenses from third parties, which are your responsibility
to obtain.

The software is provided AS-IS without warranty of any kind, including any
warranty that it is free from patent infringement.
```

#### 2. Update README.md

**Current Section to Modify:**  
Search for any language claiming "novel" or "unique" cognitive structure.

**Add New Section (after Features):**
```markdown
## What This Repository Does NOT Contain

To maintain clarity and FTO safety:
- No proprietary algorithms
- No automated reasoning engines
- No patented cognitive architectures
- No autonomous agent logic

This is a template framework only. All reasoning is user-driven.

## Patent Notice

This project is provided **without any express or implied patent license**.
Users are responsible for ensuring their own compliance with applicable patent
requirements.
```

#### 3. Verify Language

**Safe phrases to use:**
- ✅ "Template framework"
- ✅ "Markdown-based schemas"
- ✅ "Organizational structure"
- ✅ "Five-layer conceptual model"

**Phrases to avoid:**
- ❌ "Novel cognitive architecture"
- ❌ "New kind of knowledge system"
- ❌ "Breakthrough organizational model"

**Status:** ⚪ Not started  
**Effort:** 1-2 hours  
**Priority:** LOW (can wait until other modules are done)

---

## 📦 MODULE 2: aurelion-memory-lite

### Current Status
⚠️ Medium risk - contains some risky language about "novel" architecture

### Required Changes

#### 1. Add PATENT_NOTICE File
**File:** `modules/memory/aurelion-memory-lite/PATENT_NOTICE`  
(Same content as Kernel - see above)

#### 2. Update README.md - Critical Language Changes

**Current Risky Language (Examples to Find and Fix):**

❌ **REMOVE:**
```markdown
"Novel 5-floor cognitive architecture for AI-ready knowledge"
"Advanced automatic relationship detection"
"Breakthrough knowledge graph system"
"First-ever spatial memory organization"
```

✅ **REPLACE WITH:**
```markdown
"A markdown-based knowledge organization framework using a five-layer
conceptual structure inspired by library architecture."

"Graph-based relationship mapping between markdown files using NetworkX.
Relationships are detected through cross-references and metadata links."

"Knowledge storage and retrieval using standard open-source tools
(NetworkX, PyYAML, ChromaDB)."
```

#### 3. Add Safety Disclaimers

**Add Section After Features:**
```markdown
## Technology Stack

This module uses well-established open-source libraries and common patterns:

- **NetworkX** - Standard graph traversal and relationship mapping
- **PyYAML** - Standard YAML parsing
- **ChromaDB** (Premium) - Standard vector database with RAG
- **OpenAI Embeddings** (Premium) - Standard text embeddings

No proprietary algorithms or patented techniques are implemented.

## What This Repository Does NOT Contain

To ensure FTO safety:
- ❌ No proprietary memory algorithms
- ❌ No novel retrieval techniques
- ❌ No patented hybrid RAG systems
- ❌ No autonomous agent logic

All functionality uses standard, well-known patterns.

## Patent Notice

This project is provided **without any express or implied patent license**.
Users are responsible for ensuring their own compliance with applicable patent
requirements.
```

#### 4. Premium Edition Considerations

**In Memory-Premium README, emphasize standard practice:**
```markdown
## Premium Features

Premium Edition adds:
- Vector database support (ChromaDB/Pinecone)
- Semantic search using OpenAI embeddings
- Standard RAG (Retrieval-Augmented Generation) pipeline

These features use publicly available APIs and established open-source
libraries. This is a reference implementation of common patterns, not a
proprietary system.
```

**Files to Modify:**
- [ ] `modules/memory/aurelion-memory-lite/README.md`
- [ ] `modules/memory/aurelion-memory-premium/README.md` (future)
- [ ] `modules/memory/aurelion-memory-lite/PATENT_NOTICE` (create)

**Status:** ⚪ Not started  
**Effort:** 3-4 hours  
**Priority:** MEDIUM

---

## 📦 MODULE 3: aurelion-advisor-lite

### Current Status
⚠️ Medium trademark risk - "ADVISOR" is widely used  
⚠️ Must rename or always use "AURELION ADVISOR"

### Required Changes

#### 1. Naming Strategy Decision (CRITICAL)

**Option A: Always Prefix (Recommended)**
- Marketing: "AURELION ADVISOR"
- Module name: `aurelion-advisor-lite` ✅ (already safe)
- Documentation: Always say "AURELION ADVISOR" or "the ADVISOR module"

**Option B: Rename to ADVISOR-8**
- References 8-dimension framework (if applicable)
- More unique and defensible
- Module name stays: `aurelion-advisor-lite`

**Option C: Alternative Name**
- **AURELION GUIDE**
- **AURELION NAVIGATOR**
- **AURELION PLANNER**

**Decision Required By:** March 1, 2026

#### 2. Update All Documentation

**Files to Update:**
- [ ] All module READMEs that mention "ADVISOR"
- [ ] Main ecosystem README.md
- [ ] ARCHITECTURE.md
- [ ] HANDOFF.md
- [ ] Repository strategy docs

**Search/Replace Pattern:**
```
OLD: "ADVISOR module"
NEW: "AURELION ADVISOR module"

OLD: "the ADVISOR framework"
NEW: "the AURELION ADVISOR framework"

OLD: "Advisor Liteity"
NEW: "AURELION Advisor Liteity"
```

**Keep:**
- Module names: `aurelion-advisor-lite` ✅
- File paths: No changes needed
- Variable names in code: Can stay as `advisor`

#### 3. Add PATENT_NOTICE File
**File:** `modules/advisor/aurelion-advisor-lite/PATENT_NOTICE`  
(Same content as Kernel)

#### 4. Update README.md

**Add Clarity Section:**
```markdown
# AURELION Advisor (Lite Edition)

> Part of the AURELION Ecosystem by RealmCore Technologies

AURELION Advisor provides structured templates for planning, documentation,
investigation workflows, and personal development. It is a template-based
framework, not an automated planning system.

## What This Is

- ✅ Planning and documentation templates
- ✅ Investigation workflow frameworks
- ✅ Personal development structures
- ✅ Methodology documentation system

## What This Is NOT

- ❌ Not an automated planning engine
- ❌ Not a cognitive reasoning system
- ❌ Not a proprietary algorithm
- ❌ Not an AI orchestration tool

This is a template library. All planning and decision-making is user-driven.

## Patent Notice

This project is provided **without any express or implied patent license**.
```

#### 5. Files Created This Session

**Already created (need FTO updates):**
- [ ] `modules/advisor/aurelion-advisor-lite/architecture/AAI_5_Floor_Architecture.md`
- [ ] `modules/advisor/aurelion-advisor-lite/architecture/Executive_Overview.md`
- [ ] `modules/advisor/aurelion-advisor-lite/architecture/Floor_Mapping_Guide.md`
- [ ] `modules/advisor/aurelion-advisor-lite/templates/Career_Master_Template.md`
- [ ] `modules/advisor/aurelion-advisor-lite/templates/Hub_Index_Template.md`
- [ ] `modules/advisor/aurelion-advisor-lite/templates/Skills_Inventory_Template.md`
- [ ] `modules/advisor/aurelion-advisor-lite/templates/Project_Investigation_Template.md`

**FTO Updates Needed:**
- Change "AAI" references based on naming decision
- Add disclaimers about templates vs algorithms
- Remove any novelty claims

**Status:** ⚪ Not started  
**Effort:** 4-6 hours  
**Priority:** HIGH (trademark issue)

---

## 📦 MODULE 4: aurelion-agent-lite

### Current Status
⚠️ High risk - multi-agent orchestration is patent-heavy  
✅ Strategy: Keep Lite Tier as templates ONLY

### Required Changes

#### 1. README.md Structure (NEW - module not yet created)

**Create FTO-Safe README from Template:**
```markdown
# AURELION Agent (Lite Edition)

> Part of the AURELION Ecosystem by RealmCore Technologies

A curated library of prompt patterns, collaboration protocols, and session
management templates for working with LLM-based assistants like ChatGPT,
Claude, and GitHub Copilot.

## What This Repository Contains

This is a **template and documentation library**:

- ✅ 100+ curated prompts
- ✅ AI interaction protocols
- ✅ Session continuity templates
- ✅ Conversation mode patterns
- ✅ Best practices for LLM collaboration

## What This Repository Does NOT Contain

To maintain clear licensing boundaries and FTO safety:

- ❌ No multi-agent orchestration (Business tier only)
- ❌ No autonomous decision loops
- ❌ No governance workflows
- ❌ No proprietary algorithms
- ❌ No automated reasoning engines

All orchestration, governance, and multi-agent coordination logic is kept in
the separate, licensed Business tier (aurelion-agent-business).

## Technology

This module is pure documentation - markdown files containing:
- Prompt templates
- Protocol descriptions
- Example workflows

No code execution. No algorithms. User-driven only.

## Business Edition

Advanced features available separately under BSL 1.1:
- Multi-agent orchestration
- Approval workflows
- PII detection
- Cost tracking
- Team prompt libraries

See aurelion-agent-business (private repository).

## Patent Notice

This project is provided **without any express or implied patent license**.
Users are responsible for ensuring their own compliance with applicable patent
requirements.
```

#### 2. Code Separation Rules

**Lite Tier (MIT) - WHAT TO INCLUDE:**
```
✅ Markdown prompt templates
✅ YAML configuration schemas
✅ Protocol documentation
✅ Example workflows (text)
✅ Best practices guides
```

**Lite Tier (MIT) - WHAT TO EXCLUDE:**
```
❌ Multi-agent coordination code
❌ Orchestration engines
❌ Governance logic
❌ Approval workflow code
❌ Agent pipeline implementations
```

**Business Tier (BSL - Private) - CONTAINS:**
```
✅ All orchestration logic
✅ Multi-agent pipelines
✅ Governance workflows
✅ PII detection engines
✅ Cost tracking algorithms
```

#### 3. Sanitization from Memory_Engine

**When extracting prompts from Memory_Engine:**
- [ ] Remove company-specific examples (LexisNexis, RELX)
- [ ] Remove personal IP/confidential data
- [ ] Generalize work-specific prompts
- [ ] Curate 100 best (from 850+)
- [ ] Create generic demonstration examples

**Status:** ⚪ Not started (Q2 2026 planned)  
**Effort:** 8-12 hours  
**Priority:** HIGH

---

## 📦 MODULE 5: AURELION-NEXUS-PREMIUM

### Current Status
🚨 HIGH RISK - overlaps with Inworld AI, Stanford Generative Agents  
✅ Already deployed to fly.io - need careful documentation updates

### Required Changes

#### 1. Update README.md - Critical Risk Mitigation

**Current Risky Areas:**
- Memoria Engine descriptions
- NPC memory system claims
- Event cascade descriptions

**Required Changes:**

**Add Technology Clarity Section:**
```markdown
## Technology Stack

AURELION Nexus uses standard, publicly available technologies:

### Core Libraries
- **LangChain** (v0.1.0+) - Standard LLM orchestration
- **ChromaDB** (v0.4.0+) - Open-source vector database
- **OpenAI API** - Public API for GPT-4
- **FastAPI** - Standard web framework
- **Python** - Standard simulation patterns

### Architectural Patterns
- JSON-based state management (common practice)
- Event-driven simulation (established pattern)
- RAG for semantic retrieval (standard technique)
- LLM-powered NPC conversations (public API usage)

**This is a reference implementation of well-known patterns, not a novel
cognitive architecture or proprietary simulation engine.**
```

**Remove/Replace Novelty Claims:**

❌ **REMOVE:**
```markdown
"Novel Memoria Engine"
"Advanced character memory system"
"Breakthrough NPC architecture"
"First-ever semantic world simulation"
```

✅ **REPLACE WITH:**
```markdown
"Character memory management using standard JSON persistence"
"NPC conversations powered by OpenAI GPT-4"
"Semantic lore retrieval using ChromaDB RAG pipeline"
"Event-driven world simulation using common state-machine patterns"
```

#### 2. Add Safety Disclaimers

**Add Section:**
```markdown
## What This Repository Does NOT Contain

To ensure FTO safety and clear licensing:

- ❌ No patented NPC memory architectures
- ❌ No proprietary simulation algorithms
- ❌ No novel event cascade systems
- ❌ No hierarchical behavior trees (patent-heavy)

All functionality uses:
- ✅ Standard open-source libraries
- ✅ Public APIs (OpenAI)
- ✅ Well-established simulation patterns
- ✅ Common JSON state management

## Patent Notice

This software is provided **without any express or implied patent license**.

Users are responsible for:
- Ensuring compliance with applicable patent laws
- Obtaining any necessary third-party patent licenses
- Understanding that LLM API usage may have separate terms

This software is provided AS-IS without warranty that it is free from patent
infringement.
```

#### 3. Memoria Engine Positioning

**Change all references to Memoria Engine:**

OLD:
```markdown
"Memoria Engine - our proprietary NPC memory system"
```

NEW:
```markdown
"Character memory system using JSON persistence and ChromaDB semantic retrieval"
```

**In technical docs:**
```markdown
## Character Memory Implementation

The character memory system uses:
- JSON files for state persistence
- ChromaDB for semantic similarity search
- OpenAI API for conversation generation
- Standard event-driven patterns for world updates

This is an integration of existing open-source tools and public APIs,
not a proprietary cognitive architecture.
```

#### 4. Business Tier Separation

**Add Clarity:**
```markdown
## Personal vs Premium vs Business

**Lite Tier (MIT):**
- Basic simulation shell
- JSON state management
- No AI integration

**Premium Tier (MIT):**
- LLM-powered NPCs
- Semantic lore retrieval
- Single-world simulation

**Business Tier (BSL - Private):**
- Multi-campaign orchestration
- Advanced event cascades
- Integration with other Business modules
- Proprietary orchestration logic

The Business tier contains proprietary integration algorithms kept private
as trade secrets.
```

#### 5. Files to Modify

- [ ] `modules/nexus/aurelion-nexus-premium/README.md`
- [ ] `modules/nexus/aurelion-nexus-premium/DM_QUICKSTART.md`
- [ ] `modules/nexus/aurelion-nexus-premium/PATENT_NOTICE` (create)
- [ ] Any marketing materials referencing Memoria Engine

**Status:** ⚪ Not started  
**Effort:** 6-8 hours  
**Priority:** CRITICAL (already deployed, highest risk)

---

## 📦 MODULE 6: AURELION-AAI-COMPLETE

### Current Status
🚨 CRITICAL - "AAI" acronym must be renamed or always prefixed

### Required Changes

#### 1. Naming Decision (MUST BE MADE FIRST)

**This depends on global AAI naming strategy from FTO_ACTION_PLAN.md**

**Option A: Rename to AAI**
- Module becomes: `aurelion-aai-complete`
- "Autonomous Agentic Intelligence Complete"
- Update all references: AAI → AAI

**Option B: Always use AURELION prefix**
- Module stays: `aurelion-AAI-complete`
- Marketing: "AURELION Autonomous Agentic AI Complete"
- Never use "AAI" alone

**Option C: Alternative name**
- `aurelion-apex-complete` (Autonomous Personal EXperience)
- `aurelion-aria-complete` (Autonomous Reasoning & Intelligence Architecture)
- `aurelion-complete-v1` (drop acronym entirely)

**Decision Required:** March 1, 2026

#### 2. README.md (When Created Q3/Q4 2026)

**FTO-Safe Template:**
```markdown
# AURELION [AAI/AAI/Name] Complete

> The integrated AURELION ecosystem - pre-configured and ready to use

AURELION Complete combines the Kernel, Memory, Advisor, and Agent modules
into a unified system with production-ready configurations and workflows.

## What This Is

An **integration layer and reference implementation**:
- Pre-configured module integration
- Production-ready workflows
- Example modes (Strategic Advisor, Research Assistant)
- Optimized parameters

## What This Is NOT

- ❌ Not a patented invention
- ❌ Not a novel cognitive architecture
- ❌ Not a proprietary AI system
- ❌ Not a black-box algorithm

This is a **curated integration** of the open-source AURELION modules with
tested configurations and workflows.

## Architecture

AURELION Complete consists of:
- `aurelion-kernel` - Knowledge schema (MIT)
- `aurelion-memory` - Storage & retrieval (MIT)
- `aurelion-advisor` - Planning framework (MIT)
- `aurelion-agent` - AI collaboration (MIT)
- Integration layer (BSL 1.1)

The integration layer contains workflow orchestration and configuration
management, but no patented algorithms.

## Patent Notice

This software is provided **without any express or implied patent license**.
```

**Status:** ⚪ Not yet created (Q3/Q4 2026)  
**Effort:** 4-6 hours (when created)  
**Priority:** CRITICAL (naming decision)

---

## 🔧 Implementation Workflow

### Week 1: Decisions & Planning
1. [ ] Make AAI naming decision (AAI vs AURELION AAI vs alternative)
2. [ ] Make ADVISOR branding decision (AURELION ADVISOR vs ADVISOR-8)
3. [ ] Review this specification
4. [ ] Prioritize module order

### Week 2: High-Priority Modules
1. [ ] NEXUS updates (highest risk, already deployed)
2. [ ] ADVISOR updates (trademark issue)
3. [ ] Create PATENT_NOTICE template file

### Week 3: Medium-Priority Modules
1. [ ] MEMORY updates
2. [ ] AGENT preparation (for Q2 launch)
3. [ ] Global AAI/AAI rename (if needed)

### Week 4: Low-Priority & Polish
1. [ ] KERNEL updates
2. [ ] AAI-Complete naming (for Q3/Q4)
3. [ ] Final review of all changes

### Week 5: Verification
1. [ ] Search all docs for novelty claims
2. [ ] Verify PATENT_NOTICE in all MIT repos
3. [ ] Verify clear OSS/BSL boundaries
4. [ ] Review with legal (optional but recommended)

---

## 📊 Effort Estimation

| Module | Effort | Priority | Deadline |
|--------|--------|----------|----------|
| NEXUS | 6-8 hrs | CRITICAL | March 15 |
| ADVISOR | 4-6 hrs | HIGH | March 20 |
| AGENT | 8-12 hrs | HIGH | April 15 |
| MEMORY | 3-4 hrs | MEDIUM | March 30 |
| KERNEL | 1-2 hrs | LOW | April 15 |
| AAI-Complete | 4-6 hrs | CRITICAL | June 1 |
| **Total** | **26-38 hrs** | | **April 15** |

---

## ✅ Success Criteria

**For each module, verify:**
- [ ] PATENT_NOTICE file present (if MIT)
- [ ] README contains "What this does NOT contain" section
- [ ] README contains Patent Notice section
- [ ] No novelty claims in any documentation
- [ ] Clear OSS vs Business tier boundaries
- [ ] Uses safe, generic language
- [ ] Emphasizes standard tools and patterns
- [ ] Avoids patent-risky terminology

---

## 📞 Support & Questions

**If uncertain about specific language:**
1. Check FTO_Summary.md for examples
2. Default to more conservative/safer language
3. When in doubt, emphasize "standard practice" and "reference implementation"
4. Avoid any claims of uniqueness or novelty

**For trademark questions:**
- Always use "AURELION" prefix in marketing
- File trademarks for "AURELION [Module]" format
- Never use AAI standalone

---

**Last Updated:** February 16, 2026  
**Next Review:** After naming decisions (March 1, 2026)
