# AURELION Kernel (Business Edition)

> **Part of the AURELION Ecosystem**  
> **Built on AAI:** Autonomous Agentic AI Framework  
> 📋 **Status:** Planned - Multi-entity cognitive architecture

The Business Edition extends the kernel to support multiple entities: organizations, teams, projects, and people. Designed for teams, consultancies, and businesses managing complex multi-entity knowledge systems.

**AURELION** = **A**utonomous **U**niversal **R**easoning **E**ngine with **L**ong-term **I**ntelligence, **O**perational Memory & **N**eural Nexus

---

## 🎯 What's Different from Personal?

### Lite Edition
- Single-person focus
- Career and personal knowledge
- Individual entity

### Business Edition (This Module)
- **Multi-entity support**: Organizations, Teams, Projects, People
- **Entity-agnostic templates**: Reusable for any entity type
- **Relationship mapping**: Cross-entity connections
- **Access control ready**: Designed for role-based access
- **Collaborative workflows**: Team knowledge management

---

## 🏗️ Architecture

### Entity Types

```
business-kernel/
├── Entities/
│   ├── Organizations/
│   │   └── [org-name]/
│   │       ├── Floor_01_Foundation/
│   │       ├── Floor_02_Systems/
│   │       ├── Floor_03_Networks/
│   │       ├── Floor_04_Action/
│   │       └── Floor_05_Vision/
│   │
│   ├── Teams/
│   │   └── [team-name]/
│   │       └── [5 floors...]
│   │
│   ├── Projects/
│   │   └── [project-name]/
│   │       └── [5 floors...]
│   │
│   └── People/
│       └── [person-name]/
│           └── [5 floors...]
│
└── Shared/
    ├── templates/           # Entity templates
    ├── relationships/       # Cross-entity relationships
    └── standards/          # Organizational standards
```

### The 5 Floors (Entity-Agnostic)

**Floor 01 - Foundation**
- Org: Company history, capabilities, org chart
- Team: Team charter, roles, current projects
- Project: Scope, timeline, stakeholders
- Person: Career history, skills, role

**Floor 02 - Systems**
- Org: SOPs, standards, compliance
- Team: Team processes, rituals
- Project: Methodology, workflows
- Person: Personal systems, practices

**Floor 03 - Networks**
- Org: Partner ecosystem, market position
- Team: Stakeholder map, dependencies
- Project: External collaborators
- Person: Professional network

**Floor 04 - Action**
- Org: Templates, RFPs, frameworks
- Team: Sprint templates, ceremonies
- Project: Deliverables, milestones
- Person: Project assignments, tasks

**Floor 05 - Vision**
- Org: Strategy, culture, values
- Team: Team vision, goals
- Project: Success criteria, outcomes
- Person: Career trajectory, aspirations

---

## 🚀 Getting Started

### Prerequisites
- Understanding of [aurelion-kernel-lite](../aurelion-kernel-lite/)
- Multi-entity knowledge management needs
- Business/team use case

### Quick Start

**Coming Soon:** This module is under development.

**For now:** Use [aurelion-kernel-lite](../aurelion-kernel-lite/) for individual entities.

**Want to help?** We're designing this collaboratively. See [CONTRIBUTING.md](../../../docs/guides/contributing.md)

---

## 📊 Use Cases

### Consultancy
- Track multiple client orgs
- Manage consultant profiles (People)
- Project knowledge bases
- Cross-project insights

### Startup/Small Business
- Company knowledge base (Org)
- Team documentation (Teams)
- Product/feature knowledge (Projects)
- Employee profiles (People)

### Large Team
- Department structure (Org)
- Working groups (Teams)
- Initiatives (Projects)
- Team member profiles (People)

---

## 🔗 AURELION Ecosystem

This Kernel module is part of the larger AURELION Ecosystem:

**Kernel Tiers:**
- **[aurelion-kernel-lite](../aurelion-kernel-lite/)** ✅ - Single-person (MIT)
- **[aurelion-kernel-business](../aurelion-kernel-business/)** (this module) 📋 - Multi-entity (BSL)

**Pair with:**
- **[aurelion-memory-business](../../memory/aurelion-memory-business/)** - Multi-user storage
- **[aurelion-nexus-business](../../nexus/aurelion-nexus-business/)** - Team orchestration

**See the [main README](../../../README.md) for the complete ecosystem overview.**

---

## 📄 License

**Business Source License (BSL) 1.1**

- ✅ Source code is available and viewable
- ✅ Free for non-commercial use
- ✅ Free for companies under $X revenue/year
- ⚠️ Commercial use above threshold requires license
- 🔄 Converts to Apache 2.0 after 2 years

See [LICENSE](LICENSE) for full details.

**Why BSL?**
- Transparency: Code is visible
- Community: Non-commercial users can benefit
- Sustainability: Commercial users support development

---

## 🏢 Commercial Licensing

For commercial use or enterprise support:
- 📧 Email: licensing@[domain]
- 🌐 Website: [coming soon]
- 💬 Contact: See ecosystem README for details

Enterprise license includes:
- Commercial usage rights
- Priority support
- Customization assistance
- Training and onboarding

---

## 🛠️ Development Status

**Phase:** Planning  
**Target:** Q2 2026  
**Progress:** Architecture design in progress

See [ROADMAP.md](../../../ROADMAP.md) for timeline.

---

## 📖 Documentation

- [Module Integration Guide](../../../docs/guides/module-integration.md)
- [Business Edition Design Doc](../../../docs/planning/business-edition-design.md) (coming soon)
- [Entity Type Guide](../../../docs/guides/entity-types.md) (coming soon)

---

**Ready for multi-entity knowledge management?** Stay tuned for updates! 🚀
