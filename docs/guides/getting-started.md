# Getting Started with AURELION Lite Tier
**Quick installation guide for ADVISOR and AGENT modules**

**Last Updated:** February 17, 2026  
**Time Required:** 15-30 minutes  
**Prerequisites:** Text editor (VS Code, Obsidian, Typora, or any Markdown editor)

---

## 🎯 What You're Installing

**ADVISOR-Lite:** Personal knowledge management templates (10 templates + examples)  
**AGENT-Lite:** AI collaboration framework (100 prompts + 2 protocols)

Both modules are **local files** - no cloud services, no accounts needed, no dependencies.

---

## Installation Methods

### Method 1: Manual Download (Easiest)

**For ADVISOR:**

1. **Navigate to templates directory:**
   ```
   modules/advisor/aurelion-advisor-lite/templates/
   ```

2. **Create your personal directory:**
   ```bash
   # Windows
   mkdir %USERPROFILE%\Documents\my-advisor
   
   # Mac/Linux
   mkdir ~/Documents/my-advisor
   ```

3. **Copy templates you want to use:**
   - Start with these 4: `Hub_Index_Template.md`, `Career_Master_Template.md`, `Skills_Inventory_Template.md`, `Daily_Operations_Template.md`
   - Add others as needed: `Project_Investigation_Template.md`, `Network_Map_Template.md`, etc.

4. **Rename for your use:**
   ```
   Hub_Index_Template.md → 00_Hub_Index.md
   Career_Master_Template.md → 01_Career_Master.md
   Skills_Inventory_Template.md → 02_Skills_Inventory.md
   Daily_Operations_Template.md → 03_Daily_Operations.md
   ```

**For AGENT:**

1. **Bookmark these files in your browser or editor:**
   - `modules/agent/aurelion-agent-lite/prompts/README.md` (100-prompt index)
   - `modules/agent/aurelion-agent-lite/prompts/Essential_Prompt_Library.md` (46 detailed prompts)
   - `modules/agent/aurelion-agent-lite/protocols/Strategic_Advisor_Protocol.md`
   - `modules/agent/aurelion-agent-lite/protocols/Session_Management_Guide.md`

2. **No copying needed** - reference directly from repository or bookmark in your AI tool for quick copy-paste

---

### Method 2: Git Clone (For developers)

```bash
# Clone repository
git clone https://github.com/aurelion-project/aurelion-eco.git
cd aurelion-eco

# For ADVISOR - copy templates to your workspace
mkdir ~/my-advisor
cp modules/advisor/aurelion-advisor-lite/templates/*.md ~/my-advisor/

# For AGENT - bookmark or keep in repo
# (No installation needed, just reference the files)
```

---

### Method 3: Integration with Existing Systems

**Obsidian Users:**

1. Create folder in your Obsidian vault: `AURELION/`
2. Copy ADVISOR templates into `AURELION/advisor/`
3. Create note with links to AGENT prompt files (external links work in Obsidian)
4. Use Obsidian's graph view to visualize connections between your ADVISOR documents

**Notion Users:**

1. Create AURELION workspace in Notion
2. Create pages for each ADVISOR template
3. Copy template content from `.md` files to Notion pages
4. Create AGENT database with prompt library (manual entry or paste)
5. Use Notion's linked databases to connect ADVISOR docs

**VS Code Users:**

1. Open aurelion-eco repository in VS Code
2. Use workspace folders to keep ADVISOR templates separate
3. Install Markdown Preview Enhanced extension
4. Use VS Code's search to quickly find AGENT prompts when needed
5. Consider VS Code's built-in Markdown editing for ADVISOR documents

**Plain Text / Any Editor:**

1. Copy `.md` files to your documents folder
2. Open with any text editor (Notepad++, Sublime, TextEdit, etc.)
3. Markdown is readable as plain text - formatting is optional
4. Consider using a Markdown preview tool if you want formatting

---

## First Steps After Installation

### For ADVISOR (15 minutes)

**Step 1: Look at the example first (5 min)**
```bash
# Open Alex Thompson case study
modules/advisor/aurelion-advisor-lite/examples/alex_thompson_data_analyst/README.md
```

Skim these files to see how templates are filled out:
- `00_Hub_Index_Simplified.md` - Navigation structure
- `01_Career_Master_Alex_Thompson.md` - Career planning example
- `02_Skills_Inventory_Alex_Thompson.md` - Skills tracking example

**Step 2: Fill out Hub Index (5 min)**
Open your `00_Hub_Index.md` and:
- List your "Most Used" documents (just the 4 core templates for now)
- Describe your daily/weekly review workflow (simple bullets)
- Note today's date as your start date

**Step 3: Quick Career Master (5 min)**
Open your `01_Career_Master.md` and answer:
- Current role:
- Role I want in 1 year:
- Top career goal this quarter:
- One skill I need to develop:

**✅ Done!** You have a working foundation.

---

### For AGENT (20 minutes)

**Step 1: Read Strategic Advisor Protocol (10 min)**
```bash
modules/agent/aurelion-agent-lite/protocols/Strategic_Advisor_Protocol.md
```

Focus on these sections:
- "When AI Should Question You" (6 triggers)
- "Conversational Modes" (8 modes)
- "Pre-Session Thinking" (prepare before AI conversation)

**Step 2: Find your role's Top 10 prompts (5 min)**
```bash
modules/agent/aurelion-agent-lite/prompts/README.md
```

Scroll to "Role-Specific Quick-Start Guides" and find your role:
- Data Analysts
- Project Managers
- Software Engineers
- Managers/Leaders
- New to AI (if first time using AI strategically)

**Step 3: Try one prompt now (5 min)**
1. Open your AI tool (ChatGPT, Claude, GitHub Copilot Chat, etc.)
2. Pick one prompt from your role's Top 10
3. Copy it from `Essential_Prompt_Library.md` (46 detailed templates)
4. Customize with your context
5. Run it and see the difference

**✅ Done!** You're now using prompts strategically.

---

## Verification Checklist

After installation, verify you can access:

**ADVISOR:**
- [ ] Can open and edit your personal templates
- [ ] Hub Index lists your active documents
- [ ] Reviewed at least one example file (Alex Thompson)
- [ ] Filled in minimum content for 1-2 templates

**AGENT:**
- [ ] Bookmarked or know location of prompt README
- [ ] Read Strategic Advisor Protocol
- [ ] Identified your role's Top 10 prompts
- [ ] Tested 1 prompt with your AI tool

---

## Optional: Set Up Daily/Weekly Workflows

### Daily Workflow (15 minutes)

**Morning (10 min):**
1. Open ADVISOR `Daily_Operations.md`
2. Review yesterday's wrap-up
3. Brain dump today's tasks
4. Use AGENT "Priority Matrix" prompt to order tasks strategically
5. Time block your top 3 priorities

**Evening (5 min):**
1. Update `Daily_Operations.md` with completed tasks
2. Note blockers encountered
3. Log one win (for career documentation later)
4. Prep tomorrow's context

---

### Weekly Review (30 minutes)

**Friday afternoon or Sunday evening:**

1. **ADVISOR Review:**
   - Open Hub Index
   - Check Career Master - progress on quarterly goals?
   - Update Skills Inventory - what did you learn/apply this week?
   - Review active projects

2. **AGENT Reflection:**
   - Use "Retrospective Analysis" prompt:
     ```
     "This week I accomplished [list]. Challenges: [list].
     Help me: identify patterns, spot wins to document, 
     adjust next week's priorities."
     ```

3. **Document Insights:**
   - Update relevant ADVISOR templates with AI insights
   - Capture any new prompts or workflows that worked well

---

## Storage & Sync Recommendations

### Local Storage (Simplest)

**Store templates in:**
- Windows: `C:\Users\[YourName]\Documents\AURELION\`
- Mac: `~/Documents/AURELION/`
- Linux: `~/Documents/AURELION/`

**Backup strategy:**
- Manual: Copy folder weekly to external drive
- Automated: Use built-in backup (Time Machine, File History, etc.)

---

### Cloud Sync (Convenient)

**Good options:**
- **OneDrive/Google Drive/Dropbox:** Auto-sync across devices
- **iCloud Drive:** Mac users
- **Syncthing:** Privacy-focused, self-hosted

**Setup:**
1. Create AURELION folder in synced directory
2. Copy templates there
3. Access from any device with sync

**Warning:** Be careful with sensitive work content in cloud storage (check company policy).

---

### Version Control (Advanced)

**For developers or power users:**

```bash
# Initialize git in your personal AURELION folder
cd ~/my-advisor
git init
git add .
git commit -m "Initial AURELION setup"

# Optional: Push to private GitHub repo
git remote add origin https://github.com/[you]/my-advisor.git
git push -u origin main
```

**Benefits:**
- Full history of changes
- Revert to previous versions
- Work from multiple computers
- Never lose content

**Privacy:** Use PRIVATE repository if content contains work details.

---

## Troubleshooting

### "I can't edit the .md files"

**Solution:**
- Install a Markdown editor (VS Code is free and excellent)
- Or use any text editor (Notepad, TextEdit, etc.) - .md files are plain text
- Or use Obsidian (free) for advanced Markdown features

---

### "The templates are overwhelming"

**Solution:**
- Start with just 3: Hub Index, Career Master, Daily Operations
- Add more templates only when you have a specific need
- You don't need to fill out every section - adapt to your needs
- Look at Alex Thompson example to see selective usage

---

### "I don't know which AGENT prompts to use"

**Solution:**
- Start with your role's "Top 10" from README.md
- Try 2-3 prompts per week (don't try to memorize all 100)
- Most useful prompts will become habits after 2-3 uses
- Create shortcuts/bookmarks for your most-used prompts

---

### "My workflow broke down after 2 weeks"

**Solution (This is normal!):**
- Don't feel guilty - restart is common
- Use AGENT "Getting Back on Track" approach:
  ```
  "I haven't updated my system in 3 weeks. Help me restart with 
  minimal time investment. What's the simplest restart path?"
  ```
- Simplify: If 10 templates was too much, use 3
- Focus on Daily Operations first - rebuild from there

---

###"Where should I store sensitive work content?"

**Solution:**
- Option 1: Keep work content in local-only folder (no cloud sync)
- Option 2: Sanitize content in templates (use role names like "Manager" instead of real names)
- Option 3: Separate repos: Work content (local only), Personal content (synced)
- Option 4: Use encryption (VeraCrypt, BitLocker) for sensitive work folder

**IMPORTANT:** Check your company's data policy before storing work content in personal systems.

---

## Integration Guide

**Want to use ADVISOR + AGENT together?**

See: [ADVISOR + AGENT Integration Guide](advisor-agent-integration.md)

Shows how to:
- Fill ADVISOR templates using AGENT prompts
- Use AGENT for strategic reflection on ADVISOR content
- Build integrated daily/weekly workflows
- Real examples: Alex Thompson's integrated usage

---

## Next Steps

**After setup:**

1. **Week 1:** Build daily habit with Daily Operations template
2. **Week 2:** Add Career Master and set one quarterly goal
3. **Week 3:** Try 5-10 AGENT prompts in real work situations
4. **Week 4:** Weekly review routine - reflect and refine your system

**Join the community:**
- GitHub Discussions: Ask questions, share workflows
- Discord: Coming Q2 2026
- Contribute: Share your custom prompts or template adaptations

---

**Questions?**

- Documentation: See `/docs/guides/` folder
- Examples: See `/modules/advisor/aurelion-advisor-lite/examples/`
- Issues: GitHub Issues
- Discussions: GitHub Discussions

---

**Last Updated:** February 17, 2026  
**Version:** 1.0  
**Part of:** AURELION Lite Tier

---

*Start simple, build gradually, adapt freely. The best system is the one you actually use.*
