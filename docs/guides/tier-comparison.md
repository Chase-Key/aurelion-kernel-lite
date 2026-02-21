# AURELION Tier Comparison Guide

## Overview

AURELION uses a three-tier system across 5 modules, designed around **natural paywalls** and **transparent licensing**. All code is visible, but different tiers have different requirements and licenses.

**The 5 Modules:**
- **Kernel** - Cognitive structure (5-floor framework)
- **Memory** - Storage & retrieval (file → vector DB)
- **Advisor** - Strategic planning (career GPS, methodology library)
- **Agent** - AI collaboration (prompts, protocols, governance)
- **Nexus** - World simulation (story engine, AI NPCs)

**Repository Strategy (Hybrid Approach):**
- 10/13 repos are **public** (77% visibility) - All Personal, all Premium, Kernel-Business, Memory-Business
- 3/13 repos are **private** (23% enterprise IP) - Advisor-Business, Agent-Business, Nexus-Business
- **Fair balance:** Open source community gets everything they need, only enterprises pay for advanced integration

**Note:** AGENT has only Personal and Business tiers (no Premium) - Personal is feature-complete for individuals.

---

## 🆓 Lite Tier (Free & Open)

### Philosophy
**"Build trust through complete openness"**

Free for everyone, forever. MIT licensed means you can do anything with it. No hidden features, no artificial limitations.

### Who It's For
- Individuals
- Students
- Hobbyists
- Career development
- Small-scale worldbuilding
- Learning and experimentation

### What You Get

| Module | What It Does | Requirements |
|--------|--------------|--------------|
| **Kernel Lite** | 5-floor knowledge structure | Just a text editor |
| **Memory Lite** | File-based storage + knowledge graph | Python 3.9+ |
| **Advisor Lite** | Career planning + methodology library | Just a text editor |
| **Agent Lite** | 100 prompts + AI interaction protocols | Just a text editor |
- **Hosting:** Self-hosted only
- **Cost:** $0/month

### License
**MIT License** - Fully open source

```
✅ Commercial use
✅ Modification
✅ Distribution
✅ Private use
```

### Limitations (By Design)
- Single user only
- No AI features
- Manual world management
- Basic search capabilities
- No semantic understanding

**These aren't artificial limits** - this is what makes sense for personal use without infrastructure costs.

---

## ⭐ Premium Tier (Paid Services Required)

### Philosophy
**"Open code + natural paywall = trust + sustainability"**

The code is MIT licensed and fully visible, but you need paid services to run it. This creates a natural tier separation while maintaining transparency.

### Who It's For
- D&D DMs (serious campaigns)
- Professional writers
- Researchers & investigators
- Power users
- Anyone wanting AI-powered features

### What You Get

| Module | What It Does | Requirements |
|--------|--------------|--------------|
| **Memory Premium** | Vector DB + semantic search | Pinecone ($70+/mo) or self-host Chroma |
| **Advisor Premium** | AI knowledge graph + semantic search | OpenAI API ($30-100/mo) |
| **Nexus Premium** | AI NPCs + world engine | OpenAI API ($30-100+/mo) |

**Note:** AGENT has no Premium tier - Lite Edition is feature-complete for individuals.
- Semantic search with embeddings
- Investigation tracking workflows
- Methodology mapping
- Timeline reconstruction
- Pattern detection
- Unlimited API usage

**Advisor Premium:**
- AI-powered knowledge graph generator
- Semantic methodology search
- Progress tracking dashboards
- Template auto-population
- Python CLI for automation
- Career gap analysis
- ROI: Save 104 hours/year ($5,200 value)

**Nexus Premium:**
- **Complete Stonecrest Campaign** (showcase!)
- GPT-4 powered NPC conversations
- ChromaDB semantic lore retrieval
- RAG (Retrieval Augmented Generation)
- Character memory systems
- FastAPI web interface
- 24/7 deployment ready

### Technical Specs
- **Storage:** Vector DB (Pinecone/Chroma)
- **Search:** Semantic similarity, embeddings
- **AI:** GPT-4, embeddings (OpenAI)
- **Hosting:** Self-hosted or fly.io
- **Cost:** $70-150/month (infrastructure costs)

### License
**MIT License** (Same as Personal!)

The code is fully open source. You're paying for:
- OpenAI API access (you need this for GPT-4)
- Pinecone subscription (or self-host Chroma)
- More compute resources

**Natural Paywall:** You literally cannot use these features without paying for the services they require.

### Why It's Not Free
```
Premium Features require:
├── OpenAI API
│   ├── GPT-4 for NPCs: ~$0.03-0.06 per conversation
│   ├── Embeddings: ~$0.0001 per 1K tokens
│   └── Estimated: $30-100/month for active use
│
└── Vector Database
    ├── Pinecone: $70/month (managed)
    └── OR Chroma: Free but self-host costs
```

### Upgrade Path
1. Start with Lite Tier (free)
2. Test the concept, build familiarity
3. When you need AI features, upgrade
4. Pay for infrastructure, not software

---

## 🏢 Business Tier (Commercial License)

### Philosophy
**"Source available + commercial license = transparency + sustainability"**

All code is visible (BSL), but commercial use above a threshold requires a license. After 2 years, converts to Apache 2.0.

### Who It's For
- Teams & startups
- Consultancies
- Professional DM services
- Gaming companies
- Businesses managing shared knowledge

### What You Get

| Module | What It Does | Commercial Threshold |
|--------|--------------|---------------------|
| **Kernel Business** | Multi-entity (orgs, teams, projects) | Requires license |
| **Memory Business** | Multi-user + collaboration + RBAC | Requires license |
| **Advisor Business** | Team knowledge hubs + onboarding | Requires license |
| **Agent Business** | Multi-agent orchestration + governance | Requires license |
| **Nexus Business** | Multi-campaign management | Requires license |

### Key Features

**Kernel Business:**
- Multi-entity support (Organizations, Teams, Projects, People)
- Entity-agnostic templates
- Cross-entity relationship mapping
- Access control ready
- Collaborative workflows

**Memory Business:**
- Multi-user support
- Role-based access control (RBAC)
- Team permissions
- Audit trails
- Collaborative editing
- Organizational memory graph
- Distributed architecture

**Advisor Business:**
- Team knowledge hubs with RBAC
- Onboarding automation
- Compliance frameworks (SOC 2, HIPAA)
- Analytics and usage tracking
- Cross-team methodology sharing
- ROI: Save $500K+ annually (100-person consulting firm)

**Agent Business:**
- Multi-agent orchestration (5+ agent pipelines)
- Team prompt libraries (version-controlled)
- Approval workflows
- PII detection and compliance
- Usage analytics and cost tracking
- ROI: 7.6x typical return

**Nexus Business:**
- Multi-campaign management
- Team collaboration (multiple DMs)
- Campaign templates
- Player/customer management
- Analytics dashboard
- Professional DM tools

### Technical Specs
- **Everything from Premium +**
- Authentication & authorization
- Multi-tenancy
- Audit logging
- Distributed systems
- Team coordination
- **Cost:** $300-1000+/month (infrastructure) + license fee

### License
**Business Source License (BSL) 1.1**

```
✅ Source code visible
✅ Free for non-commercial use
✅ Free for companies < $[THRESHOLD] revenue/year
⚠️ Commercial use above threshold → license required
🔄 Converts to Apache 2.0 after 2 years
```

### Why BSL?
1. **Transparency:** Code is visible, not hidden
2. **Hobbyist-friendly:** Free for non-commercial use
3. **Small business-friendly:** Free under revenue threshold
4. **Sustainable:** Large commercial users support development
5. **Eventually open:** Becomes Apache 2.0 after 2 years

### Commercial License Includes
- ✅ Commercial usage rights
- ✅ Priority support
- ✅ Customization assistance
- ✅ Training and onboarding
- ✅ SLA guarantees
- ✅ Migration assistance

### Pricing (TBD)
Contact for enterprise licensing:
- Solo Pro: $X/month
- Small team: $Y/month
- Enterprise: Custom

---

## 🔄 Upgrade Paths

### From Personal → Premium

**When to upgrade:**
- You want AI-powered NPCs
- You need semantic search
- You're a professional DM
- Investigation tracking is valuable

**What changes:**
- Your data structure stays the same
- Add vector DB
- Add OpenAI API keys
- Everything else works the same

**Migration:** Simple - Personal data imports directly

### From Premium → Business

**When to upgrade:**
- You need multi-user support
- You're running a business
- Team collaboration required
- Multiple campaigns/projects

**What changes:**
- Add authentication
- Add team permissions
- Commercial license required
- More infrastructure

**Migration:** Contact for assistance

### Can You Mix Tiers?

**Yes!** Common patterns:

```
Individual Knowledge Worker:
├── Kernel Lite (free cognitive structure)
├── Advisor Premium (AI career planning)
├── Agent Lite (AI collaboration protocols)
└── Memory Premium (semantic search)

Serious D&D DM:
├── Kernel Lite (free structure)
├── Agent Lite (AI prompts)
└── Nexus Premium (AI NPCs + Stonecrest)

Professional Team:
├── Kernel Business (multi-entity)
├── Memory Business (team collaboration)
├── Advisor Business (knowledge hubs)
├── Agent Business (multi-agent governance)
└── Nexus Premium (AI NPCs)
```

---

## 💰 Cost Breakdown

### Lite Tier
```
Total: $0/month

Software: Free (MIT)
Modules: Kernel, Memory, Advisor, Agent, Nexus (all Personal)
Infrastructure: Self-hosted (your computer)
```

### Premium Tier
```
Total: $70-200/month (varies by modules used)

Software: Free (MIT)
Modules: Memory Premium, Advisor Premium, Nexus Premium

Infrastructure (varies by module):
├── OpenAI API: $30-100/month (for Advisor, Nexus)
├── Pinecone: $70/month (for Memory, or self-host Chroma)
└── Hosting: $5-20/month (if deployed)

Example Configurations:
• Advisor Premium only: $30-100/mo (OpenAI)
• Memory + Advisor: $100-170/mo (OpenAI + Pinecone)
• All 3 Premium modules: $105-190/mo
```

### Business Tier
```
Total: $299/mo per team (up to 50 users) + infrastructure

Software: License included (BSL)
Modules: Any Business edition (Kernel, Memory, Advisor, Agent, Nexus)

Infrastructure (per team):
├── Everything from Premium: $70-190/month
├── Auth service: $30-100/month
├── Database: $50-200/month
├── Team hosting: $100-500+/month
├── Compliance (SOC 2, HIPAA): Included
└── Priority support: Included

Total: $549-1189/month per team (50 users)
Per user: ~$11-24/month

Volume Discounts:
• 2-5 teams: 10% off
• 6-10 teams: 20% off
• 11+ teams: Custom pricing
```

---

## 🤔 Choosing the Right Tier

### Start with Personal if:
- [ ] You're an individual
- [ ] You don't need AI features (or just want AI prompts)
- [ ] You want to test the concept
- [ ] You're learning or experimenting
- [ ] Budget is $0
- [ ] Agent Lite is feature-complete for solo AI collaboration

### Upgrade to Premium if:
- [ ] You want AI-powered career planning (Advisor Premium)
- [ ] You need semantic knowledge search (Memory Premium)
- [ ] You want AI NPCs for worldbuilding (Nexus Premium)
- [ ] Investigation tracking is valuable
- [ ] You're okay paying ~$100-190/month
- [ ] You're a serious knowledge worker, DM, or power user

### Consider Business if:
- [ ] You have a team (5+ people)
- [ ] Multiple people need shared access
- [ ] You need multi-agent governance (Agent Business)
- [ ] You need team knowledge hubs (Advisor Business)
- [ ] You're running a commercial operation
- [ ] You need audit trails and compliance
- [ ] You need RBAC and approval workflows
- [ ] You want priority support and SLAs
- [ ] You manage $299/mo per team budget

---

## 📄 License Comparison Table

| Aspect | MIT (Personal/Premium) | BSL (Business) |
|--------|------------------------|----------------|
| **View source** | ✅ Yes | ✅ Yes |
| **Modify** | ✅ Yes | ✅ Yes (non-commercial) |
| **Commercial use** | ✅ Yes | ⚠️ License required |
| **Redistribute** | ✅ Yes | ✅ Yes (with license) |
| **Sub-license** | ✅ Yes | ❌ No |
| **Revenue limit** | ❌ None | ⚠️ $[THRESHOLD]/year |
| **Becomes fully open** | Already is | After 2 years |

---

## ❓ FAQ

### Why not just make everything free?
The code IS free (MIT/visible). You pay for infrastructure (OpenAI, Pinecone) that we don't control. This is more honest than hidden costs.

### Why BSL for Business tier?
We want to support development sustainably while being transparent. BSL lets hobbyists use it free, small companies use it free, and only large commercial operations need a license. Plus it becomes Apache 2.0 after 2 years.

### Can I use Personal commercially?
Yes! MIT license allows commercial use. Lite Tier is perfect for freelancers, consultants, small businesses who don't need multi-user features.

### Can I self-host Premium to avoid costs?
You can self-host Chroma (vector DB) instead of Pinecone, but you still need OpenAI API for GPT-4. That's the natural paywall - without it, the AI features don't work.

### What if I exceed the Business threshold?
Contact us for a commercial license. We're reasonable - pricing is designed to be accessible.

### Will prices change?
Personal stays free forever (MIT). Premium "cost" is just infrastructure you pay directly to providers. Business licensing will be finalized before release.

### Can I contribute to all tiers?
Yes! All code is visible. We welcome contributions to all tiers.

---

## 🚀 Getting Started

**Ready to choose?**

1. **Personal:** Download any module and start using
2. **Premium:** Start with Personal, then add API keys when ready
3. **Business:** Contact us to discuss your needs

See the [main README](../README.md) for links to all modules.

---

**Questions?** See [FAQ](../docs/guides/faq.md) or reach out to the maintainers.

---

## 🔑 Quick Decision Matrix

| Your Situation | Recommended Path |
|---------------|------------------|
| Solo knowledge worker, career planning | Advisor Lite → Premium |
| Individual using AI heavily | Agent Lite (free!) |
| D&D DM, casual worldbuilding | Nexus Lite → Premium |
| Investigative researcher | Memory Lite → Premium |
| Consulting team (5-50 people) | Advisor Business + Agent Business |
| Software eng team (10-200 people) | Memory Business + Agent Business |
| Multi-campaign D&D business | Nexus Business |

---

**Last Updated:** February 16, 2026 (Updated for 5-module ecosystem)
