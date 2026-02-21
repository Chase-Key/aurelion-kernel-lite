# Phase 1 Launch: Simple GitHub Setup

**Launch:** February 17, 2026  
**What:** 5 Lite modules → One public repository  
**Time:** 15 minutes

---

## What Gets Launched

### ✅ Phase 1 (Today)
- KERNEL-Lite v1.0.0
- MEMORY-Lite v1.0.0  
- ADVISOR-Lite v0.2.0
- AGENT-Lite v0.2.0
- NEXUS-Lite v0.1.0

All MIT licensed, free forever.

### 🔒 Staying Private (For Now)
- Premium modules (launch in Phase 2 - Q3 2026)
- nexus-premium (stays private forever - has production keys)

**Already protected:** `.gitignore` excludes all premium modules.

---4-Step Launch Process

### Step 1: Create GitHub Repository (2 minutes)

**On GitHub.com:**

1. Go to: https://github.com/new
2. **Repository name:** `aurelion-eco`
3. **Description:** `Modular AI ecosystem: cognitive structure, memory systems, planning frameworks, and agent collaboration`
4. **Visibility:** ✅ Public
5. **DO NOT check:** "Add a README" or "Add .gitignore" or "Choose a license"
6. Click **Create repository**
7. **Copy the URL shown** (looks like: `https://github.com/YOUR-USERNAME/aurelion-eco.git`)

**Expected Output:** Should show lines excluding premium modules.

---Step 2: Initialize and Push (3 minutes)

**In PowerShell, run these commands:**

```powershell
# Navigate to your project
cd "c:\Users\chase\.vscode\Personal Projects\aurelion-eco"

# Initialize git
git init

# Stage all files (.gitignore protects premium modules)
git add .

# VERIFY: This should show ZERO results (no premium files)
git status | Select-String "premium"

# If you see premium files above, STOP and check .gitignore
# If empty (good!), continue:

# Make first commit
git commit -m "Phase 1: AURELION Ecosystem - 5 Lite Modules

Releasing 5 MIT-licensed modules:
- KERNEL-Lite v1.0.0 (cognitive structure)
- MEMORY-Lite v1.0.0 (knowledge graph)
- ADVISOR-Lite v0.2.0 (planning templates)
- AGENT-Lite v0.2.0 (collaboration prompts)
- NEXUS-Lite v0.1.0 (simulation framework)

Phase 2 (Q3 2026): Premium modules
Phase 3: Business tier announcements"

# Connect to GitHub (use YOUR username in the URL)
git remote add origin https://github.com/YOUR-USERNAME/aurelion-eco.git

# Set branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

**If asked for credentials:**
- Username: Your GitHub username
- Password: Use a Personal Access Token (see Step 4 if needed)heck which files are tracked
git ls-tree -r main --name-only | Select-String "premium"  # Should be EMPTY
```

---Step 3: Verify on GitHub (2 minutes)

**Go to your repository:** `https://github.com/YOUR-USERNAME/aurelion-eco`

**✅ Check that you see:**
- 5 Lite module folders: `kernel`, `memory`, `advisor`, `agent`, `nexus`
- `README.md` displays with tier comparison table
- `docs/` folder with guides
- `shared/` folder with licenses

**❌ Verify you DON'T see:**
- Any folders ending in `-premium`
- Any `.env` files
- Any `sk-proj-` strings (use GitHub search)

**If you see premium modules or secrets:** Delete the repo immediately, fix `.gitignore`, and start over.

**Example:** `https://github.com/chase/aurelion-eco.git`

---Step 4: Configure Repository (optional, 2 minutes)

**On GitHub.com:**

1. Go to repository **Settings** → **About** (main page, click gear icon)
2. Add **Topics:** `ai`, `cognitive-architecture`, `knowledge-management`, `agent-framework`, `planning-tools`
3. Check ✅ **Releases** and ✅ **Packages**
4. Savepowershell
git branch -M main


Should show your commit with hash.

-- GitHub Authentication (if needed)

**If Step 2 asks for password:**

### Get a Personal Access Token

1. Go to: https://github.com/settings/tokens
2. Click **Generate new token (classic)**
3. **Note:** `aurelion-eco`
4. **Expiration:** 90 days
5. Check ✅ **repo** (full control)
6. Click **Generate token**
7. **Copy it immediately** (looks like `ghp_ABC123...`)

### Use Token as Password

```
Username: YOUR-GITHUB-USERNAME
Password: [paste token here]
```

### Remember It (Windows)

```powershell
git config --global credential.helper wincred
```

Windows will save it for next time


   - [ ] Search for "api_key" (should only show template references)

6. Check ✅ **"Packages"** (for future)
7. Click **"Save changes"**

--- Updates

**After Phase 1 launch, when you want to push changes:**

```powershell
cd "c:\Users\chase\.vscode\Personal Projects\aurelion-eco"

# Make your changes to files...

# Stage and commit
git add .
git commit -m "Your update message"
git push
```

**Phase 2 (Q3 2026) - Launch Premium Modules:**

Edit `.gitignore` and remove these lines:
```
modules/memory/aurelion-memory-premium/
modules/advisor/aurelion-advisor-premium/
```

**KEEP THIS LINE FOREVER:**
```
modules/nexus/aurelion-nexus-premium/   # Has production API keys
```

Then:
```powershell
git add .
git commit -m "Phase 2: Premium modules"
git push
# Switch back to main
git checkout main
```

--- Rollback

**IF you see premium files or API keys on GitHub:**

1. **Delete repo immediately:** Go to Settings → Danger Zone → Delete
2. **Rotate any exposed keys:** https://platform.openai.com/api-keys
3. **Fix locally:**
   ```powershell
   rm -Recurse -Force .git
   # Verify .gitignore has premium exclusions
   # Start over from Step 1
   
# 6. Start over from Part 1 of this guide
100MB)
- Different modules need different release cadences
- Community requests separate packages

---

| Problem | Solution |
|---------|----------|
| "Permission denied" | Use HTTPS: `git remote set-url origin https://github.com/USER/aurelion-eco.git` |
| "Remote already exists" | Remove first: `git remote remove origin` then add again |
| "Updates rejected" | Force push: `git push -u origin main --force` |
| Password every time | Cache it: `git config --global credential.helper wincred` |powershell
git config --global credential.helper wincred
```

---✅ Launch Checklist

- [ ] Step 1: GitHub repo created
- [ ] Step 2: Pushed from local (verified no premium files)
- [ ] Step 3: Checked on GitHub (5 Lite modules visible, no secrets)
- [ ] Step 4: Added topics and description

---

**Time:** ~15 minutes  
**Result:** 5 Lite modules live on GitHub  
**Next:** Phase 2 (Q3 2026) - Premium modules

🚀 **That's it! You're launched

🚀 **Follow this guide step-by-step and you'll have AURELION Ecosystem live on GitHub!**
