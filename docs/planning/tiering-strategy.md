# Tiering Strategy

## Overview

AURELION uses a three-tier product strategy that aligns with user needs, technical constraints, and GitHub Copilot access levels.

## The Three Tiers

### Personal (Free)
**Target:** Individuals, students, hobbyists, job seekers

**Technical Constraints:** ~50 GitHub Copilot requests/month (free tier)

**Design Philosophy:** Minimize API usage, maximize offline capability, keep it simple

### Premium (Paid)
**Target:** Power users, researchers, investigators, consultants

**Technical Freedom:** Unlimited GitHub Copilot requests (paid tier)

**Design Philosophy:** Rich features, semantic understanding, advanced workflows

### Business (Team)
**Target:** Teams, startups, consultancies, small businesses

**Technical Requirements:** Multi-user, collaborative, secure

**Design Philosophy:** Organizational knowledge, access control, scalability

## Tier Comparison Matrix

### Memory Module

| Feature | Personal | Premium | Business |
|---------|----------|---------|----------|
| **Storage** | Local files | Vector DB | Distributed DB |
| **Format** | JSON/YAML/MD | Vector + files | Vector + files |
| **Search** | Keyword/regex | Semantic | Multi-entity semantic |
| **API Calls/Month** | <50 | Unlimited | Unlimited per user |
| **Context Window** | 2-4k tokens | 8-32k tokens | Variable by role |
| **Offline Mode** | ✅ Full | ⚠️ Partial | ❌ Cloud-first |
| **Investigation Tracking** | ❌ | ✅ | ✅ + Team collab |
| **Methodology Mapping** | ❌ | ✅ | ✅ + Shared |
| **Workflow Visualization** | ❌ | ✅ | ✅ + Multi-user |
| **Pattern Detection** | ❌ | ✅ | ✅ |
| **Timeline Reconstruction** | ❌ | ✅ | ✅ |
| **Multi-user Access** | ❌ | ❌ | ✅ |
| **Role-based Permissions** | ❌ | ❌ | ✅ |
| **Audit Logging** | ❌ | ❌ | ✅ |
| **Collaborative Editing** | ❌ | ❌ | ✅ |

### Kernel Module

| Feature | Personal | Business |
|---------|----------|----------|
| **Entities Supported** | 1 (you) | Multiple |
| **Floor Structure** | 5 floors | 5 floors |
| **Career Tracking** | ✅ | ✅ |
| **Skills Inventory** | ✅ | ✅ (Capabilities Matrix) |
| **Network Mapping** | ✅ Personal | ✅ Organizational |
| **Project Templates** | ✅ | ✅ |
| **ADVISOR Framework** | ✅ | ✅ (Culture Framework) |
| **Multi-entity Support** | ❌ | ✅ |
| **Cross-entity Linking** | ❌ | ✅ |
| **Access Control** | N/A | ✅ |
| **Entity Types** | Person only | Person, Org, Team, Project |
| **Relationship Graphs** | ❌ | ✅ |

### Nexus Module

| Feature | Personal | Premium | Business |
|---------|----------|---------|----------|
| **Agent Types** | Single agent | Multi-agent | Team agents |
| **Routing** | Basic | Intelligent | Distributed |
| **Workflows** | Simple | Complex | Collaborative |
| **Orchestration** | ❌ | ✅ | ✅ Advanced |
| **Multi-user Coordination** | ❌ | ❌ | ✅ |

### Sim Module

| Feature | Personal | Premium | Business |
|---------|----------|---------|----------|
| **Testing Environment** | Local | Local/Cloud | Cloud |
| **Scenarios** | Basic | Complex | Multi-user |
| **Benchmarking** | Basic | Advanced | Advanced |
| **Team Testing** | ❌ | ❌ | ✅ |

## Technical Architecture by Tier

### Lite Tier Architecture

```
User/Agent
    ↓
Local Kernel (Markdown templates)
    ↓
Local Memory (File system)
    ├── JSON files
    ├── YAML configs
    └── Markdown docs
    ↓
Keyword Search (regex/grep)
    ↓
Response (local only)
```

**Key Characteristics:**
- Zero external dependencies
- Works completely offline
- Fast local search
- Git-friendly
- Manual organization
- Budget-friendly (free)

### Premium Tier Architecture

```
User/Agent
    ↓
Kernel (Schema validation)
    ↓
Nexus (Query routing & orchestration)
    ↓
Memory (Vector DB)
    ├── Embedding generation
    ├── Chroma/Pinecone
    ├── Semantic search
    └── File cache (offline backup)
    ↓
Advanced Features
    ├── Investigation tracking
    ├── Methodology mapping
    ├── Workflow visualization
    └── Pattern detection
    ↓
Rich Response
```

**Key Characteristics:**
- Vector DB for semantic search
- Intelligent query routing
- Advanced workflows
- Real-time updates
- Cloud-connected (offline mode available)
- Unlimited API usage

### Business Tier Architecture

```
Multiple Users/Agents
    ↓
API Gateway
    ├── Authentication (OAuth/SAML)
    ├── Authorization (RBAC)
    └── Rate limiting
    ↓
Multi-entity Kernel
    ↓
Nexus (Multi-agent coordination)
    ↓
Distributed Memory
    ├── Vector DB (shared)
    ├── Entity stores
    ├── Access control layer
    └── Audit logging
    ↓
Collaborative Features
    ├── Team knowledge graphs
    ├── Cross-entity relationships
    ├── Real-time updates
    └── Conflict resolution
    ↓
Response (role-appropriate)
```

**Key Characteristics:**
- Multi-user support
- Role-based access control
- Organizational structure
- Team collaboration
- Compliance & audit
- Scalable infrastructure

## Use Cases by Tier

### Lite Tier Use Cases

**Career Development**
- Track job history
- Document skills and projects
- Prepare for interviews
- Build portfolio

**Freelancing**
- Manage client work
- Track project history
- Skills inventory
- Time tracking

**Learning & Growth**
- Document learning journey
- Track courses and certifications
- Build knowledge base
- Personal development

**Side Projects**
- Organize project ideas
- Track progress
- Document decisions
- Maintain context

### Premium Tier Use Cases

**Investigation Work** (CK's primary use case)
- Track complex investigations
- Map relationships and patterns
- Timeline reconstruction
- Evidence organization

**Research**
- Literature review management
- Methodology tracking
- Hypothesis testing
- Data organization

**Consulting**
- Client engagement tracking
- Recommendation history
- Reusable methodologies
- Knowledge reuse across clients

**Complex Project Management**
- Multi-phase projects
- Dependency tracking
- Risk management
- Historical analysis

### Business Tier Use Cases

**Team Knowledge Management**
- Centralized team knowledge
- Onboarding new members
- Best practices documentation
- Institutional memory

**Agency/Consultancy**
- Client portfolio management
- Multi-project tracking
- Team collaboration
- Resource allocation

**Startup Operations**
- Company knowledge base
- Process documentation
- Team coordination
- Growth tracking

**Department Documentation**
- SOPs and procedures
- Team structure
- Cross-team dependencies
- Compliance documentation

## Upgrade Paths

### Personal → Premium

**Triggers for upgrade:**
- Need semantic search
- Complex investigations
- Advanced workflows
- Pattern detection needs
- API limits reached

**Migration process:**
1. Export personal file-based data
2. Generate embeddings
3. Import to vector DB
4. Enable premium features
5. Maintain file backup

**Estimated time:** 1-2 hours

### Premium → Business

**Triggers for upgrade:**
- Multiple users needed
- Team collaboration
- Access control required
- Audit trails needed
- Organizational knowledge management

**Migration process:**
1. Define entity structure
2. Create organizational schema
3. Migrate personal data to entity
4. Set up access control
5. Configure team features

**Estimated time:** 1 week (includes team setup)

## Pricing Strategy (Proposed)

### Lite Tier
**Price:** FREE
- Unlimited users
- Open source
- Community support
- GitHub-based
- Self-hosted

### Premium Tier
**Price:** $10-20/month per user
- Advanced features
- Semantic search
- Investigation tools
- Email support
- Cloud hosting optional

### Business Tier
**Price:** $50-100/user/month
- Multi-user access
- Team collaboration
- Admin controls
- Priority support
- Dedicated hosting
- SLA available

**Enterprise:** Custom pricing
- SSO/SAML
- Compliance features
- Dedicated support
- Custom integrations
- On-premise option

## Feature Development Priority

### Phase 1: Personal (March 2026)
Focus on solid, simple, offline-capable foundation

### Phase 2: Premium (April-May 2026)
Build on CK's investigation workflow (proven use case)

### Phase 3: Business (June-July 2026)
Add multi-user and collaborative features

## Success Metrics

### Lite Tier
- Active users
- GitHub stars
- Community contributions
- Template variety

### Premium Tier
- Conversion rate from personal
- Feature usage
- User satisfaction (NPS)
- Retention rate

### Business Tier
- Team size
- Seats per organization
- Revenue per account
- Enterprise pipeline

## Why This Tiering Works

### 1. Aligned with Real Constraints
GitHub Copilot free tier = 50 requests/month
→ Design for minimal API usage (Lite Tier)

GitHub Copilot paid tier = unlimited
→ Enable rich features (premium tier)

### 2. Natural Progression
```
Individual exploration → Power user → Team adoption
    (Personal)              (Premium)     (Business)
```

### 3. Validated by CK's Journey
CK's actual progression:
1. Started with basic memory (personal use case)
2. Evolved to complex investigations (premium use case)
3. Potential team/org expansion (business use case)

This IS the user journey!

### 4. Clear Value Props

**Personal:** "Start free, build your cognitive kernel"
**Premium:** "Unlock the investigation workflow CK uses"
**Business:** "Create organizational memory"

### 5. Sustainable Revenue
- Free tier attracts users
- Premium converts power users
- Business scales revenue
- Each tier pays for itself

---

**Decision Date:** February 16, 2026  
**Status:** Approved & In Development  
**Last Updated:** February 16, 2026
