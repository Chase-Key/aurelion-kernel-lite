# Naming Strategy

## Problem Statement

Original AURELION naming used single-letter suffixes (aurelion-k, aurelion-m, aurelion-n, aurelion-s) which caused:
- Memorization burden
- Poor discoverability
- Unclear purpose to newcomers
- SEO challenges

## Solution: Full Names + Descriptive Suffixes

### Core Modules (Full Names)
✅ **Use full, descriptive names:**

- `aurelion-memory` (not aurelion-m)
- `aurelion-kernel` (not aurelion-k)
- `aurelion-nexus` (already good)
- `aurelion-sim` (already good)

**Benefits:**
- Self-documenting
- No memorization required
- Better for search engines
- Professional appearance

### Tier Suffixes (Use Case Based)

**Selected Approach:** Use case focused (Option 1)

```
aurelion-{module}-{tier}

Where tier is:
- personal    # Individual use, free tier
- premium     # Power users, paid tier  
- business    # Teams/orgs, team tier
```

**Examples:**
```
aurelion-kernel-lite
aurelion-kernel-business
aurelion-memory-lite
aurelion-memory-premium
aurelion-memory-business
```

### Alternative Approaches Considered

**Option 2: Scope/Scale Focused**
```
aurelion-kernel-solo
aurelion-kernel-team
aurelion-kernel-enterprise
```
❌ Rejected: Less clear about use case

**Option 3: Abbreviations**
```
aurelion-kernel-1p   (1 person)
aurelion-kernel-biz  (business)
aurelion-kernel-pro  (professional)
```
❌ Rejected: Still requires memorization

## Naming Matrix

| Module | Personal | Premium | Business |
|--------|----------|---------|----------|
| **Kernel** | aurelion-kernel-lite | N/A* | aurelion-kernel-business |
| **Memory** | aurelion-memory-lite | aurelion-memory-premium | aurelion-memory-business |
| **Nexus** | aurelion-nexus-lite | aurelion-nexus-premium | aurelion-nexus-business |
| **Sim** | aurelion-sim | aurelion-sim | aurelion-sim |

*Kernel premium same as personal with optional enhancements

## Future Variants

### Domain-Specific Kernels
```
aurelion-kernel-academic     # Research/education
aurelion-kernel-creative     # Artists/makers
aurelion-kernel-legal        # Legal professionals
aurelion-kernel-medical      # Healthcare
```

### Special Purpose Modules
```
aurelion-kernel-template     # Base template
aurelion-kernel-enterprise   # Large org edition
aurelion-memory-offline      # Fully offline variant
```

## URL Structure

### GitHub Repositories
```
github.com/{org}/aurelion-kernel-lite
github.com/{org}/aurelion-kernel-business
github.com/{org}/aurelion-memory-lite
github.com/{org}/aurelion-memory-premium
github.com/{org}/aurelion-memory-business
```

### Documentation URLs
```
docs.aurelion.io/kernel/personal
docs.aurelion.io/kernel/business
docs.aurelion.io/memory/personal
docs.aurelion.io/memory/premium
docs.aurelion.io/memory/business
```

## Package Names

### Python
```python
pip install aurelion-memory-lite
pip install aurelion-memory-premium
pip install aurelion-kernel-lite
```

### Node.js
```bash
npm install @aurelion/MEMORY-Lite
npm install @aurelion/memory-premium
npm install @aurelion/KERNEL-Lite
```

## Internal References

### In Documentation
✅ Use full names: "aurelion-kernel-lite"  
❌ Avoid: "aurelion-k" or "the kernel"

### In Code
```python
from aurelion.memory.personal import Memory
from aurelion.kernel.personal import Kernel
```

### In Conversation
- "The personal kernel" ✅
- "KERNEL-Lite" ✅
- "aurelion-k" ❌

## Migration Plan

### Rename Existing
```
aurelion-k → aurelion-kernel-lite
aurelion-m → aurelion-memory-lite (when created)
```

### Update References
- [ ] README files
- [ ] Internal links
- [ ] Import statements
- [ ] Documentation
- [ ] Examples

## Brand Consistency

### AURELION (Main Brand)
- Always capitalized: AURELION
- Full form in introductions
- Acronym: Autonomous Universal Reasoning Engine with Long-term Intelligence, Operational Memory & Neural Nexus

### Module Names
- Lowercase in URLs/repos: aurelion-kernel-lite
- Sentence case in prose: Aurelion Kernel Lite
- Title case in headings: AURELION Kernel - Lite Edition

### Taglines
- **AURELION:** "Cognitive Architecture for Autonomous AI"
- **Kernel:** "Knowledge Organization Schema"
- **Memory:** "Persistent Storage & Retrieval"
- **Nexus:** "Agent Orchestration Layer"
- **Sim:** "Testing & Simulation Framework"

## Rationale

### Why Full Names?
1. **Discoverability:** Users searching "aurelion memory" will find it
2. **Clarity:** Purpose immediately clear
3. **Professional:** Looks more polished
4. **Memorable:** "memory" easier than "m"

### Why Use Case Suffixes?
1. **Target Audience:** Clear who it's for
2. **Feature Set:** Implies capabilities
3. **Upgrade Path:** personal → premium → business
4. **Extensibility:** Easy to add new variants

### Why Not Versions?
❌ `aurelion-kernel-v1`, `aurelion-kernel-v2`
- Versions are orthogonal to editions
- Each edition will have its own versioning
- Use cases don't change, features do

## Examples in Context

### Marketing Copy
```
"Get started with AURELION Kernel Lite—the free, 
individual edition perfect for career development."
```

### Technical Docs
```
Install the personal memory module:
pip install aurelion-memory-lite
```

### README Title
```markdown
# AURELION Kernel - Lite Edition
```

### Repository Description
```
aurelion-kernel-lite: Personal knowledge management 
cognitive kernel for individual professionals
```

---

**Decision Date:** February 16, 2026  
**Status:** Approved & Implemented  
**Last Updated:** February 16, 2026
