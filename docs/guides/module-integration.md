# Module Integration Guide

## Overview

The AURELION Ecosystem consists of four core modules that work together to provide a complete cognitive architecture for personal and organizational knowledge management.

## Module Relationships

```
┌─────────────────────────────────────────────────────────┐
│                  AURELION ECOSYSTEM                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐         ┌──────────────┐            │
│  │   KERNEL     │ defines │   MEMORY     │            │
│  │              │────────>│              │            │
│  │  Structure   │  schema │   Storage    │            │
│  │  Templates   │         │   Retrieval  │            │
│  └──────────────┘         └──────────────┘            │
│         │                        │                     │
│         │                        │                     │
│         └────────┬───────────────┘                     │
│                  │                                     │
│                  v                                     │
│         ┌──────────────┐                              │
│         │    NEXUS     │                              │
│         │              │                              │
│         │ Orchestrates │                              │
│         │   Agents     │                              │
│         └──────────────┘                              │
│                  │                                     │
│                  v                                     │
│         ┌──────────────┐                              │
│         │     SIM      │                              │
│         │              │                              │
│         │  Simulates   │                              │
│         │    World     │                              │
│         └──────────────┘                              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Module Breakdown

### 1. KERNEL Module
**Location:** `modules/kernel/`

**Purpose:** Defines the cognitive structure and schema for knowledge organization

**Editions:**
- ✅ `aurelion-kernel-lite` - Single-person career and knowledge management
- 📋 `aurelion-kernel-business` - Multi-entity support (orgs, teams, projects)

**What it provides:**
- 5-floor architecture (Foundation, Systems, Networks, Action, Vision)
- Template structures for organizing knowledge
- Cross-reference patterns
- Personality frameworks (ADVISOR)

**Used by:** Memory module (for structure), Nexus (for agent context)

### 2. MEMORY Module
**Location:** `modules/memory/`

**Purpose:** Persistent storage and intelligent retrieval

**Editions:**
- ✅ `aurelion-memory-lite` - File-based with knowledge graph
- 📋 `aurelion-memory-premium` - Vector DB with semantic search
- 📋 `aurelion-memory-business` - Multi-user collaborative

**What it provides:**
- Storage layer for kernel-structured content
- Knowledge graph with relationship detection
- Query and retrieval APIs
- Graph traversal algorithms

**Used by:** Kernel (stores its content), Nexus (provides context for agents)

### 3. NEXUS Module
**Location:** `modules/nexus/`

**Purpose:** Agent orchestration, world simulation, and multi-agent coordination

**Implementations:**
- ✅ `aurelion-nexus` - Complete world engine with Stonecrest campaign

**What it provides:**
- LLM-powered NPC conversations (GPT-4)
- ChromaDB semantic lore retrieval (RAG)
- Character memory systems
- Event coordination
- Web interface (FastAPI)

**Uses:** Kernel (for structure), Memory (for storage), Sim (for world progression)

### 4. SIM Module
**Location:** `modules/sim/`

**Purpose:** Story-agnostic simulation framework

**Implementations:**
- ✅ `aurelion-sim` - Core simulation engine

**What it provides:**
- Time progression systems
- Event triggering
- State management
- Character journals
- World logs
- Schema validation

**Used by:** Nexus (for world simulation)

## Integration Patterns

### Pattern 1: Personal Knowledge Management
**Use Case:** Individual organizing career and knowledge

```
Kernel Lite (structure)
    ↓
Memory Lite (storage)
```

**Setup:**
1. Navigate to `modules/kernel/aurelion-kernel-lite`
2. Fill out templates (career, skills, projects)
3. Use Memory Lite to index and query

### Pattern 2: World Building & D&D
**Use Case:** DM running persistent campaign

```
Sim (world framework)
    ↓
Nexus (AI agents + NPCs)
    ↓
Memory Lite (lore storage)
```

**Setup:**
1. Define world using `modules/sim/aurelion-sim` templates
2. Configure `modules/nexus/aurelion-nexus` with campaign
3. Use Memory for lore retrieval

### Pattern 3: Complete Cognitive System
**Use Case:** Power user with full integration

```
    Kernel Lite (structure)
            ↓
    Memory Lite (storage)
            ↓
    Nexus (orchestration)
            ↓
    Sim (simulation)
```

**Setup:**
1. Structure knowledge with Kernel
2. Store with Memory
3. Create agents with Nexus
4. Simulate scenarios with Sim

## Development Workflow

### Working on a Single Module
```bash
cd modules/{module-name}/{edition-name}
# Make changes
# Test locally
```

### Working Across Modules
```bash
cd aurelion-eco
# Make changes across modules
# Update cross-references
# Test integration
```

### Adding a New Edition
Example: Creating `aurelion-kernel-business`

```bash
cd modules/kernel
mkdir aurelion-kernel-business
# Copy structure from aurelion-kernel-lite
# Adapt for multi-entity support
# Update README and cross-references
```

## Configuration Files

### Shared Schemas
**Location:** `shared/schemas/`

Cross-module data schemas go here:
- Entity schemas
- Floor structure definitions
- Event schemas
- Memory graph formats

### Shared Templates
**Location:** `shared/templates/`

Reusable templates across modules:
- World-building templates
- Project templates
- Communication templates

### Shared Utilities
**Location:** `shared/utilities/`

Helper functions used by multiple modules:
- File I/O utilities
- Graph utilities
- Validation functions

## Testing Integration

### Local Testing
```bash
# Test each module independently first
cd modules/kernel/aurelion-kernel-lite
# Run kernel tests

cd ../../memory/aurelion-memory-lite
pip install -e .
# Test memory system

cd ../../nexus/aurelion-nexus
pip install -r requirements.txt
# Test nexus

cd ../../sim/aurelion-sim
pip install -r requirements.txt
# Test sim
```

### Integration Testing
```bash
# Test cross-module functionality
cd aurelion-eco
# Create test scenario using multiple modules
```

## Common Issues

### Issue: Cross-References Breaking
**Cause:** Module moved or renamed
**Solution:** Update relative paths in README files

### Issue: Schema Mismatches
**Cause:** Different modules using different versions
**Solution:** Centralize schemas in `shared/schemas/`

### Issue: Circular Dependencies
**Cause:** Modules importing from each other
**Solution:** Use shared utilities or abstract interfaces

## Roadmap Integration Points

### Phase 0 (Current): Foundation ✅
- All core modules integrated
- Cross-references updated
- Documentation aligned

### Phase 1: Lite Editions (Next 2 Weeks)
- Create kernel-business
- Enhance MEMORY-Lite
- Document integration patterns

### Phase 2: Premium Features (Month 2)
- Add memory-premium (vector DB)
- Enhanced nexus agent coordination
- Advanced sim features

### Phase 3: Business Tier (Q1 2026)
- Multi-user support across modules
- Collaborative features
- Access control
- Team orchestration

## Next Steps

1. **Review this guide** - Understand module relationships
2. **Test each module** - Verify individual functionality
3. **Test integration** - Verify cross-module workflows
4. **Update ACTION_CHECKLIST.md** - Mark completed items
5. **Proceed with roadmap** - Begin Phase 1 development

---

**Last Updated:** February 16, 2026  
**Status:** All modules integrated, ready for Phase 1
