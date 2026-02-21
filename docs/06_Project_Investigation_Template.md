# Project Investigation Template: Reusable Framework

**Purpose:** Systematic methodology for complex investigations, applicable to anomalies, data issues, and multi-phase research projects.  
**Origin:** Evolved from TX Waller case study (Oct 2024) + NC Data Anomaly methodology (Jan 2026)  
**Last Updated:** January 24, 2026  

---

## 📋 Cross-References

**Related Documentation:**
- **Case Study Application:** See [07_TX_Waller_Research_Case.md](07_TX_Waller_Research_Case.md) for concrete methodology demonstration with real investigation example
- **Active Project:** See [08_NC_Data_Anomaly_Project.md](08_NC_Data_Anomaly_Project.md) for current multi-phase investigation using this template
- **SQL Templates:** See [SQL_Reference_Library.md](SQL_Reference_Library.md) for query templates applicable to investigation phases
- **Glossary:** See [10_Glossary.md](10_Glossary.md) for terminology related to investigations (Case, PFID, Collection Gap, Data Latency)

---

## Template Structure (4 Phases)

Use this framework for all future investigations. Phases are sequential but can overlap.

---

## Phase 1: Problem Definition & Context

### **Objective**
Clear, concise statement of what you're investigating and why.

### **Template**

```
Investigation Title: [What's the issue?]
Timeline: [When did it start? Current status?]
Collaboration: [Who else is involved?]
Status: [Discovery / Investigation / Handoff / Complete]

## Problem Statement
- **What:** [Describe the issue/anomaly in 1-2 sentences]
- **When:** [Date/timeframe discovered]
- **Impact:** [SLA risk? Data quality? Business consequence?]

## Context & Scope
- **Known Facts:** [What's certain based on current knowledge?]
- **Scope:** [What's in scope? What's explicitly out of scope?]
- **Constraints:** [Time, resource, or technical limitations?]

## Hypothesis (Initial)
- [What do you think is causing this?]
- [Why is this plausible?]
```

---

## Phase 2: Investigation Steps & Findings

### **Objective**
Systematic exploration of hypothesis; iterative refinement of understanding.

### **Template**

```
## Investigation Progress

### Step 1: [Action]
- **What:** [What did you do?]
- **Data Examined:** [What sources/systems did you check?]
- **Finding:** [What did you discover?]
- **Next Question:** [What does this raise?]

### Step 2: [Action]
- **What:** [Next investigative step]
- **Data Examined:** [Sources checked]
- **Finding:** [Result]
- **Updated Hypothesis:** [How does this change your thinking?]

### Step 3: [Action]
- [Continue pattern]

## Key Insights from Investigation
- [What does the pattern tell you?]
- [Where does evidence point?]
- [What's still uncertain?]

## Remaining Unknowns
- [What questions remain?]
- [What can't you investigate at your level?]
- [What requires escalation?]
```

---

## Phase 3: Phased Investigation Plan (For Complex Issues)

### **Objective**
Structured roadmap for extended investigations; clear phases and deliverables.

### **Template**

```
## Multi-Phase Investigation Plan

### Phase 1: [Name - e.g., "Baseline Data Assessment"]
- **Objective:** [What's this phase trying to determine?]
- **Steps:** 
  1. [Specific action]
  2. [Specific action]
  3. [Specific action]
- **Deliverable:** [What will you have when this phase completes?]
- **Success Criteria:** [How do you know phase 1 is done?]

### Phase 2: [Name - e.g., "Root Cause Identification"]
- **Objective:** [Moving deeper into investigation]
- **Depends On:** [Findings from Phase 1]
- **Steps:** [Actions in sequence]
- **Deliverable:** [Output/findings]

### Phase 3: [Name]
- [Continue pattern]

### Phase 4: [Name - e.g., "Validation & Handoff"]
- **Objective:** [Confirm findings; prepare for next team]
- **Deliverable:** [Final report/documentation]
```

---

## Phase 4: Action Items & Deliverables

### **Objective**
Specific, actionable next steps with owner assignments and success criteria.

### **Template**

```
## Action Items for [Team/Person]

### Priority 1: [High-impact action]
- **Action:** [What needs to happen?]
- **Owner:** [Who's responsible?]
- **Timeline:** [By when?]
- **Success Criteria:** [How do you know it's done?]

### Priority 2: [Action]
- [Same structure]

### Priority 3: [Action]
- [Same structure]

## Deliverables for Handoff

- [ ] [Document type] – [Description] – Owner: [Team]
- [ ] [Document type] – [Description] – Owner: [Team]
- [ ] [Query/Tool] – [Description] – Owner: [Team]

## Communication Plan
- **Interim Updates:** [Who needs to know progress? How often?]
- **Final Report:** [Audience, format, timeline]
- **Escalation Points:** [Conditions that trigger escalation; who to contact]
```

---

## SQL & Query Templates Section

### **Objective**
Production-ready queries you created during investigation, formatted for team reuse.

### **Template**

```
## Query 1: [Descriptive Name]

### Purpose
[What does this query answer?]

### Code
\`\`\`sql
[Production-ready SQL with comments]
SELECT ...
WHERE ...
-- Comment explaining logic
\`\`\`

### Parameters to Modify
- `[PLACEHOLDER]` – What should this be?
- `[DATE_RANGE]` – How to set date range?

### Expected Results
- What should query return?
- Sample output (if helpful)

### Troubleshooting
- **Error: [Common error]** → Solution
- **Empty results?** → Check [condition]

## Query 2: [Next Query]
- [Same structure]
```

---

## Why This Framework Works

### **For You (Analyst)**
✅ Prevents analysis paralysis (clear phases guide thinking)  
✅ Documents decision-making (why you took each step)  
✅ Provides replicable methodology (repeatable for similar issues)  
✅ Creates portfolio evidence (demonstrates strategic thinking)  

### **For Your Team**
✅ Clear handoff (next team knows exactly where you left off)  
✅ Reduced ramp-up time (action items are explicit)  
✅ Methodology sharing (team can replicate your approach)  
✅ Knowledge preservation (nothing lost between team members)  

### **For Leadership**
✅ Shows professional approach (structured thinking, not guessing)  
✅ Accountability points (each phase has deliverable)  
✅ Risk management (identifies scope boundaries early)  
✅ Strategic value (demonstrates problem-solving capability)  

---

## When to Use This Template

**Use for:**
- Data anomalies (volume drops, missing fields, inconsistent values)
- Performance issues (SLA risk, processing delays, collection gaps)
- Complex troubleshooting (multi-system, cross-team investigation)
- Strategic projects (Lincoln-tier research, cross-functional analysis)

**Don't use for:**
- Standard QA checks (use QA Checklist instead)
- Simple, single-step issues (would be overkill)
- Pure operational tasks (refer to Daily Operations Playbook)

**Optional use for:**
- Training new analysts (teaching methodology through example)
- Documentation improvements (process optimization)
- Certification work (demonstrating professional standards)

---

## Completed Examples

**See also:**
- [TX_Waller_Research_Case.md](TX_Waller_Research_Case.md) – Phase 1-2 example (Texas research)
- [NC_Data_Anomaly_Project.md](NC_Data_Anomaly_Project.md) – Full 4-phase example (active project)

---

## Evolution & Refinement

**Version 1.0:** Created January 24, 2026  
**Based on:** TX Waller case study + NC Data Anomaly methodology + Tim Frakes mentorship  
**Next update:** After next project completion; add learnings and improvements

---

**Related Files:** [TX_Waller_Research_Case.md](TX_Waller_Research_Case.md) | [NC_Data_Anomaly_Project.md](NC_Data_Anomaly_Project.md) | [Project Investigation Template](Project_Investigation_Template.md) | [00_Hub_Index.md](00_Hub_Index.md)
