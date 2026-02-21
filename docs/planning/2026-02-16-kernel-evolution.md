# Kernel Evolution Planning Session
**Date:** February 16, 2026  
**Participants:** CK (Chase), AI Assistant  
**Status:** Strategic Planning

## Context

CK has built a 5-floor cognitive kernel architecture (aurelion-k) focused on personal career management. During review, we identified an opportunity to evolve this into a universal system supporting multiple user types and organizational use cases.

## Key Questions Explored

### 1. How can this become a cognitive kernel for anyone and businesses?

**Original State:**
- Single-person focused (career, skills, network)
- Hardcoded personal terminology
- Individual entity only

**Evolution Strategy:**
- Shift from content → schema thinking
- Entity-agnostic terminology
- Multi-entity support (people, orgs, teams, projects)
- Polymorphic architecture

### 2. Why would a memory management system need a cognitive kernel?

**Answer:** The kernel is the **operating system for knowledge**

| Component | Role | Analogy |
|-----------|------|---------|
| Memory (AURELION-M) | Storage | Hard drive |
| Kernel (AURELION-K) | Schema & retrieval logic | Operating system |

**Without a kernel, memory is just data.** The kernel provides:
1. **Structure** - How to organize information
2. **Context** - What the information means
3. **Relationships** - How pieces connect
4. **Operations** - How to query and use it

## Naming Strategy Decision

### Problem
Original naming (aurelion-k, aurelion-m) caused confusion even for the creator.

### Solution: Full Names + Use Case Suffixes

**Core Products:**
- ✅ `aurelion-memory` (not aurelion-m)
- ✅ `aurelion-kernel` (not aurelion-k)
- ✅ `aurelion-nexus`
- ✅ `aurelion-sim`

**Kernel Variants (Option 1 - Selected):**
```
aurelion-kernel-lite    # Single person, career/life
aurelion-kernel-business    # Multi-entity, orgs/teams
aurelion-kernel-academic    # Research/education (future)
aurelion-kernel-creative    # Artists/makers (future)
```

**Rationale:**
- Self-documenting
- Clear target audience
- Extensible for future variants
- SEO/searchability
- No memorization required

## Tiering Strategy

### Key Insight: Align with User Constraints

Different users have different GitHub Copilot access levels:
- **Free:** ~50 requests/month
- **Pro/Business:** Higher/unlimited requests

This naturally maps to different architectural approaches!

### Product Tiers

#### Personal (Free Tier)
**Target:** Individuals, students, job seekers, hobbyists

**Technical Approach:**
- File-based storage (JSON/YAML)
- Keyword search, local indexing
- Aggressive caching
- Smaller context windows (2-4k tokens)
- Offline-first
- Minimal dependencies

**Use Cases:**
- Career development
- Personal knowledge management
- Portfolio organization
- Side projects

#### Premium (Paid Tier)
**Target:** Power users, researchers, investigators, consultants

**Technical Approach:**
- Vector DB (Chroma/Pinecone)
- Semantic search with embeddings
- Larger context windows (8-32k tokens)
- Real-time streaming updates
- Advanced features

**Features CK Built:**
- Investigation tracking
- Methodology mapping
- Workflow visualization
- Pattern detection
- Timeline reconstruction

**Use Cases:**
- Complex research workflows
- Investigation management
- Professional consulting
- Advanced project management

#### Business (Team/Org Tier)
**Target:** Teams, startups, consultancies, small businesses

**Technical Approach:**
- Distributed vector DB
- Multi-user access
- Role-based permissions
- Collaborative workflows
- Audit trails

**Features:**
- Multi-entity support
- Team knowledge graphs
- Organizational memory
- Integration APIs
- Access control

## Architecture Transformation

### Terminology Shift

| Current (Personal) | Universal (Business) |
|-------------------|----------------------|
| Career Master | Entity Profile / History |
| Skills Inventory | Capabilities Matrix |
| Background Story | Origin Story / Journey |
| Personality Framework | Operating Style / Culture |
| Network Map | Relationship Graph |

### Multi-Entity Structure

```
aurelion-eco/
└── modules/
    └── kernel/
        ├── aurelion-kernel-lite/
        │   └── [5 floors for individual use]
        └── aurelion-kernel-business/
            └── Entities/
                ├── People/
                │   ├── person-1/
                │   │   └── [5 floors]
                │   └── person-2/
                ├── Organizations/
                │   └── org-1/
                │       └── [5 floors]
                └── Teams/
                    └── team-1/
                        └── [5 floors]
```

### The 5 Floors (Universal)

**Floor 01 - Foundation**
- Personal: Career history, skills, daily operations
- Business: Org history, capabilities, org chart

**Floor 02 - Systems**
- Personal: Personal glossary, workflows
- Business: Company SOPs, standards, compliance

**Floor 03 - Networks**
- Personal: Professional network, mentors
- Business: Partner ecosystem, clients, market position

**Floor 04 - Action**
- Personal: Project templates, decision frameworks
- Business: Templates, RFPs, incident response

**Floor 05 - Vision**
- Personal: Career goals, working style (ADVISOR)
- Business: Company culture, strategy, values

## Memory Module Tiering

Extended the same tiering approach to aurelion-memory:

### aurelion-memory-lite
- File-based storage
- Keyword search
- <50 API calls/month
- Offline mode
- Basic CRUD

### aurelion-memory-premium
- Vector DB storage
- Semantic search
- Unlimited API calls
- Investigation tracking (CK's use case!)
- Methodology mapping
- Workflow visualization

### aurelion-memory-business
- Distributed storage
- Multi-user access
- Team collaboration
- Access control
- Audit trails

## Product Matrix

```
┌─────────────┬──────────────────┬──────────────────┬──────────────────┐
│ Module      │ Personal (Free)  │ Premium (Paid)   │ Business (Team)  │
├─────────────┼──────────────────┼──────────────────┼──────────────────┤
│ MEMORY      │ ✅ File-based    │ ✅ Vector DB     │ ✅ Multi-user    │
│             │ Keyword search   │ Semantic search  │ Collaborative    │
│             │ 50 queries/mo    │ Unlimited        │ Team permissions │
├─────────────┼──────────────────┼──────────────────┼──────────────────┤
│ KERNEL      │ ✅ 1-person      │ Same as Personal │ ✅ Multi-entity  │
│             │ Career focus     │ (enhanced opt.)  │ Orgs/teams       │
├─────────────┼──────────────────┼──────────────────┼──────────────────┤
│ NEXUS       │ 🔄 Single agent  │ 🔄 Multi-agent   │ 📋 Team agents   │
│             │ Basic routing    │ Complex workflow │ Orchestration    │
├─────────────┼──────────────────┼──────────────────┼──────────────────┤
│ SIM         │ 📋 Local sim     │ 📋 Cloud sim     │ 📋 Collab sim    │
│             │ Basic testing    │ Complex scenarios│ Team testing     │
└─────────────┴──────────────────┴──────────────────┴──────────────────┘
```

## Ecosystem Strategy (This Decision!)

### Problem
Managing multiple related repositories becoming complex. Need unified workspace for:
- Documentation
- Planning sessions
- Development coordination
- Shared resources

### Solution: aurelion-eco (Umbrella Repository)

**Structure:**
```
aurelion-eco/
├── docs/              # All documentation & planning
│   ├── planning/      # Strategy sessions (like this!)
│   ├── architecture/  # Technical design docs
│   └── guides/        # Development guides
├── modules/           # All AURELION modules
│   ├── memory/
│   ├── kernel/
│   ├── nexus/
│   └── sim/
└── shared/            # Shared resources
    ├── templates/
    ├── schemas/
    └── utilities/
```

**Benefits:**
- Single entry point for entire ecosystem
- Centralized documentation
- Easier cross-module development
- Preserve planning discussions
- Shared resources across modules

## Next Steps

### Immediate (Today)
1. ✅ Create aurelion-eco structure
2. ✅ Document this planning session
3. 🚧 Move aurelion-k → modules/kernel/aurelion-kernel-lite
4. 🚧 Update paths and references
5. 🚧 Create ecosystem documentation

### Short Term (This Week)
1. Create aurelion-kernel-business structure
2. Refactor templates to be entity-agnostic
3. Create tier comparison documentation
4. Plan aurelion-memory architecture

### Medium Term (This Month)
1. Implement Lite Editions (kernel + memory)
2. Document CK's investigation workflow features
3. Design premium edition features
4. Create migration guides

### Long Term (Q1 2026)
1. Release Lite Editions
2. Beta test premium features
3. Design business edition architecture
4. Build developer community

## Key Insights

1. **User's real usage = product roadmap**
   - CK started with basic memory (personal)
   - Evolved to investigations (premium)
   - This IS the natural upgrade path

2. **Technical constraints drive design**
   - API limits aren't limitations—they're product tiers
   - Different architectures for different needs

3. **Modularity enables growth**
   - Start simple (personal)
   - Add complexity as needed (premium)
   - Scale to organizations (business)

4. **Documentation is development**
   - Capturing planning sessions like this
   - Creates roadmap
   - Preserves decision context

## Decisions Made

- ✅ Use full names: aurelion-memory, aurelion-kernel (not -m, -k)
- ✅ Suffix pattern: -personal, -premium, -business
- ✅ Create aurelion-eco umbrella repository
- ✅ Three-tier product strategy (personal/premium/business)
- ✅ Apply tiering to both memory AND kernel
- ✅ Preserve 5-floor architecture across all variants
- ✅ Document planning sessions in /docs/planning/

## Open Questions

- [ ] Pricing strategy for premium/business tiers?
- [ ] Open source licensing approach per tier?
- [ ] Timeline for premium feature implementation?
- [ ] Community contribution model?
- [ ] Integration with other tools (Obsidian, Notion, etc.)?

## References

- Original kernel structure: `aurelion-k/`
- Advisor Liteity framework (included in Floor 05)
- CK's investigation workflow features (premium tier basis)

---

**Status:** Planning Complete → Ready for Implementation  
**Next Session:** Kernel restructuring and business edition creation

