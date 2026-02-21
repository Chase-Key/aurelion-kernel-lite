# Memory_Engine Classification Summary
**Date:** February 16, 2026  
**Status:** Week 1 Classification - COMPLETE ✅

---

## 📊 Inventory Results

**Total Files Found:** 177 files across multiple directories

### Top-Level Files: 83 files
- **Classification Spreadsheet:** [docs/planning/memory-engine-classification.csv](../planning/memory-engine-classification.csv)
- **Raw Inventory:** [docs/planning/memory-engine-inventory.csv](../planning/memory-engine-inventory.csv)

### Subdirectories: 4 folders (96 files)
- **Book_Project/** - 39 files, 594KB - 🔴 **EXCLUDE ENTIRELY** (Creative work)
- **Phone/** - 16 files, 520KB - 🔴 **EXCLUDE ENTIRELY** (Personal notes)
- **keycd_deliverable/** - 37 files, 402KB - 🔴 **EXCLUDE ENTIRELY** (Work deliverable)
- **.secure/** - 4 files, 22KB - 🔴 **EXCLUDE ENTIRELY** (Confidential)

---

## 🎯 Classification Breakdown

### 🟢 SAFE (20 files) - Ready to use with minimal edits
- AAI architecture files (AAI_MASTER_ARCHITECTURE.md, AAI_FLOOR_MAPPING.md)
- AI protocol files (31_AI_Agent_Interaction_Protocol.md, 24_Strategic_Advisor_Protocol.md)
- Session management (20_Session_Management_Continuation_Guide.md)
- Framework guides (32_Personal_Engine_Framework_Guide.md, 16_Engine_Executive_Overview.md)
- Copilot best practices (Copilot_Best_Practices.md)
- Reference scripts (EXTRACT_AURELION_FRAMEWORKS.ps1)

**Action:** Verify proper nouns, check for company names, minimal edits

---

### 🟡 NEEDS ANONYMIZATION (23 files) - Extract framework, sanitize examples
- **Career templates** (01_Career_Master.md, 02_Skills_Inventory.md)
- **Investigation templates** (06_Project_Investigation_Template.md, 26_Investigation_Decision_Tree.md)
- **Case studies** (07_TX_Waller_Research_Case.md, 08_NC_Data_Anomaly_Project.md)
- **Network maps** (18_Organizational_Network_Map.md)
- **Hub structure** (00_Hub_Index.md)
- **AI prompts** (AI_Prompt_Library.md - 850+ prompts, need to curate 100)
- **Memoria Engine** (36_Memoria_*, 36A_Memoria_* - belongs in Nexus-Premium)

**Action:** Remove proper nouns, anonymize examples, create generic templates

---

### 🔴 PRIVATE ONLY (3 files) - Elite Business tools, NEVER public
- **09_QA_Standards.md** → Advisor-Business (Private) - QA automation tool
- **04_Analyst_Workload_Reference.md** → Advisor-Business (Private) - Workload tracker
- **28_Chase_Key_Workload_Analysis.md** → Advisor-Business (Private) - $200K optimization

**Action:** Extract to `/aurelion-private/advisor-business/` (local storage, NOT in public repo)

---

### 🔴 REMOVE/EXCLUDE (40+ files) - Not packageable
- Company-specific (LexisNexis SOPs, RELX strategy, compliance docs)
- Personal career (Career advice, gap analysis, background story)
- Session history (Session summaries, progress trackers, handoffs)
- Work deliverables (Proposals, pilot documents)
- Personal creative work (**Book_Project/** folder - 39 files)

**Action:** Do not extract; remains in Memory_Engine only

---

## 📋 Top Priority Files for Extraction (Week 2-3)

### ADVISOR-Lite (Public) - 15 files

**Architecture (SAFE):**
1. ✅ AAI_MASTER_ARCHITECTURE.md (234 lines) - Core 5-floor framework
2. ✅ AAI_FLOOR_MAPPING.md (313 lines) - Floor structure
3. ✅ 16_Engine_Executive_Overview.md (370 lines) - Vision document
4. ✅ 17_Engine_Onboarding_Wizard.md (418 lines) - Setup guide

**Templates (NEEDS ANONYMIZATION):**
5. 🟡 00_Hub_Index.md (203 lines) → Create blank hub template
6. 🟡 01_Career_Master.md (589 lines) → Create blank career template
7. 🟡 02_Skills_Inventory.md (490 lines) → Create blank skills template
8. 🟡 06_Project_Investigation_Template.md (187 lines) → Generic template
9. 🟡 18_Organizational_Network_Map.md (461 lines) → Blank network map
10. 🟡 26_Investigation_Decision_Tree.md (278 lines) → Generic decision tree

**Examples (NEEDS ANONYMIZATION):**
11. 🟡 07_TX_Waller_Research_Case.md (196 lines) → "Project Alpha" fictional case
12. 🟡 08_NC_Data_Anomaly_Project.md (2,162 lines) → Extract template only

**Total:** ~5,600 lines to process for ADVISOR-Lite

---

### AGENT-Lite (Public) - 7 files

**Protocols (SAFE):**
1. ✅ 31_AI_Agent_Interaction_Protocol.md (514 lines) - Core protocol
2. ✅ 24_Strategic_Advisor_Protocol.md (1,076 lines) - Strategic advisor guide
3. ✅ 20_Session_Management_Continuation_Guide.md (600 lines) - Session framework
4. ✅ Copilot_Best_Practices.md (585 lines) - Copilot usage

**Prompts (NEEDS ANONYMIZATION):**
5. 🟡 AI_Prompt_Library.md (570 lines, **850+ prompts**) → Curate 100 best; remove work prompts

**Context (SAFE):**
6. ✅ AI_Context_Limitations.md (315 lines) - AI limitations

**Total:** ~3,660 lines to process for AGENT-Lite

---

### ADVISOR-Business (PRIVATE) - 3 files

**Elite Tools (PRIVATE ONLY):**
1. 🔴 09_QA_Standards.md (266 lines) → QA automation tool
2. 🔴 04_Analyst_Workload_Reference.md (265 lines) → Workload capacity framework
3. 🔴 28_Chase_Key_Workload_Analysis.md (313 lines) → $200K optimization algorithm

**Total:** ~844 lines to process for Advisor-Business (PRIVATE)

**⚠️ CRITICAL:** These files NEVER go in public repos. Store in `/aurelion-private/advisor-business/`

---

### NEXUS-Premium (Public) - 3 files

**Memoria Engine (NEEDS ANONYMIZATION):**
1. 🟡 36_Memoria_Engine_Complete_Project_Summary.md (281 lines)
2. 🟡 36A_Memoria_Technical_Implementation.md (833 lines)
3. ✅ 36B_Memoria_Lessons_Learned_Feb2026.md (371 lines)

**Total:** ~1,485 lines to process for Nexus-Premium

---

## 🔍 Proper Nouns to Remove

### People (Search & Replace)
- "Chase Key" → [Your Name] or "User"
- "Byron Koontz" → "Team Member A"
- "Melissa Autin" → "Project Manager"
- "Josefina" → [remove or generic name]
- "Rell" (Advisor Liteity) → [remove entirely]
- Any other stakeholder names in network maps

### Companies (Search & Replace)
- "LexisNexis" → "Enterprise Company" or "Data Provider"
- "RELX" → [remove]
- "Phoenix" (project) → "Project Phoenix" (generic)
- "DART" (team) → "Data Team"
- "TFS" (team) → "Technical Team"

### Systems (Search & Replace)
- "TXTRSTS" (feed) → "System Feed A"
- "UTCJDF" (system) → "Legacy System"
- "Waller County" → "Region A" or "County X"
- "Texas" / "North Carolina" → "State A" / "State B"

### Data (Remove Specifics)
- "42,188 cases" → "N records"
- "38,000 cases" → "baseline of M records"
- "$200,000 revenue" → "$X revenue" or "significant revenue"
- Specific dates → "Q1 YYYY" or "Month YYYY"

---

## ✅ Week 1 Complete - Next Steps

### Week 2-3 Tasks (Feb 24 - Mar 9)

**ADVISOR-Lite Extraction:**
- [ ] Extract AAI architecture (5 files, ~1,500 lines)
- [ ] Create 10 blank templates (Career, Skills, Hub, Network, etc.)
- [ ] Anonymize case studies (TX Waller → Project Alpha)
- [ ] Create 1 fictional example (Alex Thompson, data analyst)

**AGENT-Lite Extraction:**
- [ ] Extract AI protocols (4 files, ~2,800 lines)
- [ ] Curate 100 essential prompts from AI_Prompt_Library.md
- [ ] Remove work-specific prompts
- [ ] Organize into categories (Research, Writing, Analysis, etc.)

**ADVISOR-Business Extraction (PRIVATE):**
- [ ] Extract QA_Standards.md → `/aurelion-private/advisor-business/QA_Automation_Tool.md`
- [ ] Extract Workload files → `/aurelion-private/advisor-business/Workload_Tracker.md`
- [ ] Remove LexisNexis metrics, team names
- [ ] Store locally (NOT in git)

**NEXUS-Premium Extraction:**
- [ ] Extract Memoria Engine (3 files, ~1,500 lines)
- [ ] Sanitize examples
- [ ] Keep architecture, remove work specifics

---

### Week 4 Tasks (Mar 10-16) - Security Review

**Automated Scans:**
- [ ] Search all files for "LexisNexis" (expect 0 results)
- [ ] Search for "RELX" (expect 0 results)
- [ ] Search for "Chase Key" (expect 0 results)
- [ ] Search for "Byron" (expect 0 results)
- [ ] Search for "Waller" (expect 0 results)

**Manual Review:**
- [ ] Read all ADVISOR-Lite templates
- [ ] Read all AGENT-Lite prompts
- [ ] Verify fictional examples are generic
- [ ] Check for any remaining proper nouns

**Exclusion Verification:**
- [ ] Confirm Book_Project/ not copied
- [ ] Confirm Phone/ not copied
- [ ] Confirm keycd_deliverable/ not copied
- [ ] Confirm .secure/ not copied
- [ ] Confirm QA/Workload tools in private folder only

---

## 📂 Target Structure After Extraction

```
aurelion-eco/
├── modules/
│   ├── advisor/
│   │   ├── aurelion-advisor-lite/
│   │   │   ├── README.md ✅ (already written)
│   │   │   ├── templates/
│   │   │   │   ├── Career_Master.md (blank)
│   │   │   │   ├── Skills_Inventory.md (blank)
│   │   │   │   ├── Hub_Index.md (blank)
│   │   │   │   ├── Project_Investigation.md (blank)
│   │   │   │   ├── Network_Map.md (blank)
│   │   │   │   └── ... (5 more templates)
│   │   │   ├── examples/
│   │   │   │   └── Alex_Thompson_Case_Study.md (fictional)
│   │   │   └── architecture/
│   │   │       ├── AAI_5_Floor_Architecture.md
│   │   │       ├── Floor_Mapping.md
│   │   │       └── Executive_Overview.md
│   │   │
│   │   └── aurelion-advisor-business/ (PRIVATE - local only)
│   │       ├── QA_Automation_Tool.md
│   │       └── Workload_Tracker.md
│   │
│   ├── agent/
│   │   └── aurelion-agent-lite/
│   │       ├── README.md ✅ (already written)
│   │       ├── prompts/
│   │       │   ├── research/ (20 prompts)
│   │       │   ├── writing/ (20 prompts)
│   │       │   ├── analysis/ (20 prompts)
│   │       │   ├── strategic/ (20 prompts)
│   │       │   └── general/ (20 prompts)
│   │       ├── protocols/
│   │       │   ├── AI_Interaction_Protocol.md
│   │       │   ├── Strategic_Advisor_Protocol.md
│   │       │   └── Session_Management.md
│   │       └── guides/
│   │           ├── Copilot_Best_Practices.md
│   │           └── Context_Limitations.md
│   │
│   └── nexus/
│       └── aurelion-nexus-premium/
│           └── memoria/
│               ├── Memoria_Architecture.md
│               ├── Technical_Implementation.md
│               └── Lessons_Learned.md
```

---

## 💾 Local Private Storage (NOT in git)

```
C:\Users\chase\aurelion-private\
├── advisor-business\
│   ├── QA_Automation_Tool.md
│   └── Workload_Tracker.md
│
├── agent-business\
│   └── (Q4 2026 development)
│
└── nexus-business\
    └── (Q3 2026 development)
```

---

## 🎯 Success Metrics

### Files to Extract: 28 files
- 🟢 SAFE: 20 files (minimal edits)
- 🟡 ANONYMIZE: 23 files (heavy sanitization)
- 🔴 PRIVATE: 3 files (local storage only)

### Total Lines to Process: ~11,589 lines
- ADVISOR-Lite: ~5,600 lines
- AGENT-Lite: ~3,660 lines
- Advisor-Business (Private): ~844 lines
- Nexus-Premium: ~1,485 lines

### Files to Exclude: 153 files
- 🔴 REMOVE: 40+ top-level files
- 🔴 EXCLUDE: 4 folders (Book_Project, Phone, keycd_deliverable, .secure)

---

## ✅ Week 1 Status: COMPLETE

- [x] Located Memory_Engine directory
- [x] Created inventory (177 files)
- [x] Classified all 83 top-level files
- [x] Identified 4 subdirectories to exclude
- [x] Created classification spreadsheet
- [x] Listed proper nouns to remove
- [x] Prioritized files for extraction
- [x] Defined target structure

**Ready for Week 2: Extraction & Anonymization** 🚀

---

**Next Action:** Begin extracting ADVISOR-Lite templates (start with AAI architecture files)
