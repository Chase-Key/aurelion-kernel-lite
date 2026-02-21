# Quick Reference Guide

## AURELION Ecosystem at a Glance

### Core Modules
| Module | Purpose | Tiers |
|--------|---------|-------|
| **KERNEL** | Knowledge schema & structure | Personal, Business |
| **MEMORY** | Storage & retrieval | Personal, Premium, Business |
| **NEXUS** | Agent orchestration | Personal, Premium, Business |
| **SIM** | Testing & simulation | Universal |

### Repository Structure
```
aurelion-eco/
├── docs/              # Documentation
├── modules/           # All modules
│   ├── memory/
│   ├── kernel/
│   ├── nexus/
│   └── sim/
└── shared/            # Shared resources
```

### The 5 Floors
1. **Foundation** - Core facts & operations
2. **Systems** - Standards & procedures
3. **Networks** - Relationships & connections
4. **Action** - Templates & frameworks
5. **Vision** - Strategy & philosophy

### Naming Pattern
```
aurelion-{module}-{tier}

Examples:
- aurelion-kernel-lite
- aurelion-memory-premium
- aurelion-nexus-business
```

### Tier Quick Guide

**Personal (Free)**
- Individual use
- File-based storage
- Offline-capable
- ~50 API calls/month

**Premium (Paid)**
- Power users
- Vector DB
- Semantic search
- Unlimited API calls

**Business (Team)**
- Multi-user
- Collaborative
- Access control
- Organizational memory

### Common Commands

**Navigate to kernel:**
```bash
cd modules/kernel/aurelion-kernel-lite
```

**Navigate to memory:**
```bash
cd modules/memory/aurelion-memory-premium
```

**Open in VS Code:**
```bash
code .
```

**Initialize git:**
```bash
git init
```

### Key Documents
- [README.md](../../README.md) - Ecosystem overview
- [ARCHITECTURE.md](../../ARCHITECTURE.md) - System design
- [ROADMAP.md](../../ROADMAP.md) - Development timeline
- [Planning Session](../planning/2026-02-16-kernel-evolution.md) - Original decisions
- [Naming Strategy](../planning/naming-strategy.md) - Naming conventions
- [Tiering Strategy](../planning/tiering-strategy.md) - Tier details

### Next Steps for CK
1. Close VS Code
2. Move aurelion-k → modules/kernel/aurelion-kernel-lite
3. Open aurelion-eco in VS Code
4. Verify structure
5. Update kernel internal links
6. Initialize git
7. Create business kernel skeleton
8. Begin memory module development

### GitHub Copilot Prompts

**For personal kernel:**
- "Help me document my career starting with [ROLE]"
- "Create a skills inventory for [PROFESSION]"
- "Document a project using the template"

**For business kernel:**
- "Create an entity profile for [ORGANIZATION]"
- "Document our team structure"
- "Map our partner ecosystem"

### File Extensions
- `.md` - Markdown (documentation, templates)
- `.yaml`/`.yml` - Configuration
- `.json` - Data structures
- `.py` - Python code

### Version Control
**Current Status:** Pre-git (local only)
**Next:** Initialize git, create repo
**Branch Strategy:** feature/*, fix/*, docs/*

### Support
- Documentation: `docs/`
- Examples: Each module's `examples/` folder
- Issues: GitHub Issues (once public)
- Planning: `docs/planning/`

---

**Last Updated:** February 16, 2026  
**Quick access:** Keep this file bookmarked!
