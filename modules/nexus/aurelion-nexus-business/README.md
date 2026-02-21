# AURELION Nexus (Business Edition)

> **Part of the AURELION Ecosystem**  
> **Built on AAI:** Autonomous Agentic AI Framework  
> 📋 **Status:** Planned - Multi-campaign enterprise orchestration

The Business Edition enables professional DMs, gaming companies, and writing teams to manage multiple campaigns, collaborative worldbuilding, and team coordination. Enterprise-grade world engine with multi-user support.

**AURELION** = **A**utonomous **U**niversal **R**easoning **E**ngine with **L**ong-term **I**ntelligence, **O**perational Memory & **N**eural Nexus

---

## 🎯 What's Different?

### Lite Edition
- Single DM/worldbuilder
- Basic simulation framework
- Manual world management
- No AI integration

### Premium Edition
- Single DM/worldbuilder
- AI-powered NPCs (GPT-4)
- Semantic lore retrieval
- **Stonecrest showcase**
- Solo campaign management

### Business Edition (This Module)
- **Multi-campaign management**
- **Team collaboration** (multiple DMs, writers)
- **Shared world creation**
- **Campaign templates**
- **Analytics dashboard**
- **Customer/player management**
- **Professional DM tools**

---

## 🏗️ Architecture

### Multi-Campaign System

```
campaigns/
├── campaign-stonecrest/          # Example: CK's campaign
│   ├── dm: ck
│   ├── co-dms: [alice, bob]
│   └── players: [group1]
│
├── campaign-shadowrealm/         # Another campaign
│   ├── dm: alice
│   └── players: [group2]
│
└── shared-world/                 # Optional: Shared universe
    └── canonical-lore/
```

### Key Features

**1. Multi-Campaign Dashboard**
```python
# Campaign overview
campaigns = nexus.list_campaigns(dm=user)
for campaign in campaigns:
    print(f"{campaign.name}: {campaign.active_players} players")
```

**2. Team Collaboration**
```python
# Multiple DMs working together
campaign.add_co_dm(user_id=alice)
campaign.share_permissions(
    user=alice,
    permissions=["edit_npcs", "run_sessions", "view_analytics"]
)
```

**3. Campaign Templates**
```python
# Create from template
new_campaign = nexus.create_from_template(
    template="fantasy_political_intrigue",
    name="Court of Shadows",
    dm=user
)
```

**4. Player Management**
```python
# Track player groups
campaign.add_player_group(
    name="Friday Night Crew",
    players=[p1, p2, p3, p4],
    schedule="weekly_friday_7pm"
)
```

**5. Analytics & Insights**
```python
# Campaign analytics
stats = campaign.get_analytics(
    date_range=("2024-01-01", "2024-12-31")
)
# Returns: session count, player engagement, NPC interactions, etc.
```

---

## 🚀 Getting Started

### Prerequisites

**Infrastructure you'll need:**
- **Everything from Premium** (GPT-4, ChromaDB, etc.)
- **Multi-user authentication**
- **Campaign database** (PostgreSQL)
- **File storage** (S3 or equivalent)
- **Team coordination** features

**Total estimated cost:** $500-2000+/month depending on:
- Number of campaigns
- AI usage (GPT-4 calls)
- Storage needs
- Player count

### Installation

```bash
cd modules/nexus/aurelion-nexus-business
pip install -r requirements.txt

# Configure for production
cp .env.example .env
# Edit with production settings
```

### Deployment

```bash
# Docker deployment
docker-compose -f docker-compose.business.yml up -d

# Or managed hosting
# Contact for hosted solutions
```

---

## 🎲 Professional DM Features

### Campaign Management

**Session Planning**
```python
# Plan next session
session = campaign.create_session(
    date="2024-03-15",
    duration_hours=4,
    planned_events=["Royal banquet", "Assassination attempt"],
    prep_notes="Review noble relationships"
)
```

**Automated Prep**
```python
# Generate session prep
prep = campaign.generate_session_prep(
    based_on="last_session_notes",
    include=["NPC_summaries", "plot_threads", "potential_hooks"]
)
```

**World Consistency**
```python
# Check world consistency
issues = campaign.validate_world(
    check_for=[
        "timeline_conflicts",
        "character_contradictions",
        "lore_inconsistencies"
    ]
)
```

### Team Collaboration

**Shared Worldbuilding**
```python
# Co-create with team
campaign.enable_collaborative_editing(
    users=[dm1, dm2, writer1],
    approval_required=False  # or True for gated changes
)
```

**Version Control**
```python
# Track world changes
history = campaign.get_world_history(
    element="npc_aldric_vorn",
    include_dms=True
)
```

---

## 💼 Business Use Cases

### Professional DM Service
- Manage multiple client campaigns
- Track session schedules
- Player management
- Session recordings/notes
- Billing integration (external)

### Gaming Company
- Multiple DMs managing campaigns
- Shared world coordination
- Template library
- Analytics and metrics
- Customer relationship management

### Writing Team
- Collaborative worldbuilding
- Character coordination
- Timeline management
- Lore consistency
- Publication preparation

### TTRPG Publisher
- Campaign development
- Playtesting coordination
- Module creation
- Quality assurance
- Community campaigns

---

## 📊 Feature Comparison

| Feature | Personal | Premium | Business |
|---------|----------|---------|----------|
| AI NPCs | ❌ | ✅ | ✅ |
| Campaigns | 1 manual | 1 AI-powered | Unlimited |
| DMs | 1 | 1 | Multiple |
| Players | Unlimited | Unlimited | Managed groups |
| Templates | Basic | Advanced | Enterprise |
| Analytics | ❌ | Basic | Advanced |
| Support | Community | Email | Priority + Training |
| Hosting | Self | Self | Self or Managed |

---

## 🔗 AURELION Ecosystem

This Nexus module is part of the larger AURELION Ecosystem:

**Nexus Tiers:**
- **[aurelion-nexus-lite](../aurelion-nexus-lite/)** ✅ - Framework (MIT)
- **[aurelion-nexus-premium](../aurelion-nexus-premium/)** ✅ - AI-powered with Stonecrest (MIT)
- **[aurelion-nexus-business](../aurelion-nexus-business/)** (this module) 📋 - Multi-campaign (BSL)

**Built on:**
- **[aurelion-nexus-lite](../aurelion-nexus-lite/)** - Core simulation framework
- **[aurelion-memory-business](../../memory/aurelion-memory-business/)** - Multi-user storage

**See the [main README](../../../README.md) for the complete ecosystem overview.**

---

## 📄 License

**Business Source License (BSL) 1.1**

- ✅ Source code is available and viewable
- ✅ Free for non-commercial campaigns
- ✅ Free for small operations (under $X revenue/year)
- ⚠️ Commercial use above threshold requires license
- 🔄 Converts to Apache 2.0 after 2 years

See [LICENSE](LICENSE) for full details.

**Why BSL?**
- Professional DMs can see the code
- Hobbyists can use it free
- Commercial operations support development
- Eventually becomes fully open source

---

## 🏢 Commercial Licensing

For professional/commercial use:
- 📧 Email: licensing@[domain]
- 🌐 Website: [coming soon]
- 💬 Contact: See ecosystem README

Commercial license includes:
- Commercial usage rights
- Priority support
- Campaign migration assistance
- Training for DM teams
- Custom feature development
- SLA guarantees

**Pricing tiers:**
- **Solo Pro DM**: $X/month (up to Y campaigns)
- **Small Studio**: $X/month (up to Y DMs, Z campaigns)
- **Enterprise**: Custom pricing

---

## 🛠️ Development Status

**Phase:** Planning  
**Target:** Q2-Q3 2026  
**Progress:** Architecture design in progress

See [ROADMAP.md](../../../ROADMAP.md) for timeline.

---

## 📖 Documentation

- [Multi-Campaign Setup](docs/multi-campaign.md) (coming soon)
- [Team Collaboration Guide](docs/collaboration.md) (coming soon)
- [Professional DM Workflows](docs/pro-dm-workflows.md) (coming soon)
- [Migration Guide](docs/migration.md) (coming soon)

---

**Ready for professional campaign management?** Stay tuned for updates! 🚀
