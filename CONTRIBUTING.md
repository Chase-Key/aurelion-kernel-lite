# Contributing to AURELION
**How to contribute templates, prompts, examples, and improvements**

**Last Updated:** February 17, 2026  
**Status:** Open for community contributions  
**License:** MIT (your contributions will be MIT licensed)

---

## 🎯 Welcome Contributors!

AURELION is community-driven. We welcome contributions that make personal knowledge management and AI collaboration more accessible and effective.

**Ways to contribute:**
- 📝 **Templates:** New ADVISOR templates for different domains
- 🤖 **Prompts:** Battle-tested AGENT prompts for specific use cases
- 📚 **Examples:** Anonymized case studies showing real usage
- 📖 **Documentation:** Improve guides, fix typos, clarify instructions
- 🐛 **Bug reports:** Identify issues or confusing documentation
- 💡 **Ideas:** Suggest features or improvements

---

## 🚀 Quick Start for Contributors

### First-Time Contributors

1. **Star the repository** (shows interest, helps others find the project)
2. **Read existing templates/prompts** to understand style and structure
3. **Start small:** Fix a typo, improve one paragraph, or share one prompt
4. **Open an issue first** if you're planning major changes (avoid duplicate work)

### Before Contributing

- [ ] Read this CONTRIBUTING.md guide
- [ ] Review [Code of Conduct](CODE_OF_CONDUCT.md) (coming soon - TL;DR: be respectful)
- [ ] Check [existing issues](https://github.com/aurelion-project/aurelion-eco/issues) to avoid duplicates
- [ ] Test your contribution (if adding templates/prompts, use them first!)

---

## 📝 Contributing Templates (ADVISOR)

### What Makes a Good Template?

**Good templates are:**
- ✅ **Universal:** Applicable across domains (not company-specific)
- ✅ **Structured:** Clear sections with purpose statements
- ✅ **Practical:** People can actually fill them out and use them
- ✅ **Explained:** Include usage guidance, not just blank sections
- ✅ **FTO-safe:** No proprietary methodologies or copyrighted content

**Examples of good template contributions:**
- "Meeting Notes Template" (universal need)
- "Learning Plan Template" (skill development)
- "Feedback Log Template" (performance improvement)
- "Reading Notes Template" (knowledge retention)

**Not suitable:**
- Company-specific workflows (e.g., "Acme Corp Escalation Process")
- Proprietary methodologies under license
- Templates requiring specific software/tools
- Templates with embedded personal or company data

---

### Template Contribution Process

**Step 1: Create your template**

Use this structure:

```markdown
# [Template Name]

**Purpose:** [What this template helps you accomplish]  
**Last Updated:** [Date]  
**Scope:** [What areas this covers]

---

## 📋 Cross-References

**Related Documentation:**
- [Link to related templates]
- [Link to complementary tools]

---

## How to Use This Template

[2-3 paragraphs explaining: when to use this, what value it provides, 
how it fits into workflows]

### When to Use
- [Situation 1]
- [Situation 2]

---

## Section 1: [Section Name]

[Description of what goes in this section]

**Example:**
[Show a realistic example, not just blank fields]

---

## Section 2: [Section Name]

[Continue pattern]

---

## Customization Guide

**How to adapt:**
- [Tip 1]
- [Tip 2]

**Common variations:**
- [Role-specific adaptations]

---

**Last Updated:** [Date]  
**Template Version:** 1.0  
**Next Review:** [Date + 6 months]
```

**Step 2: Test it yourself**

- Use your template for 2-4 weeks in real work
- Refine based on what works/doesn't work
- Get feedback from 1-2 others if possible

**Step 3: Sanitize**

- Remove any personal information
- Remove company names, project codenames, real names
- Replace with generic or fictional examples
- Verify FTO compliance (no proprietary content)

**Step 4: Submit Pull Request**

```bash
# Fork repository
# Create branch
git checkout -b template/[your-template-name]

# Add your template
cp your-template.md modules/advisor/aurelion-advisor-lite/templates/

# Commit
git add .
git commit -m "Add [Template Name] for [use case]"

# Push and create PR
git push origin template/[your-template-name]
```

**Step 5: PR Description**

Include:
- **Purpose:** What problem does this solve?
- **Use case:** Who benefits from this template?
- **Testing:** How long you've used it, what feedback you received
- **FTO verification:** Confirm this is your original work or properly adapted from public sources

---

## 🤖 Contributing Prompts (AGENT)

### What Makes a Good Prompt?

**Good prompts are:**
- ✅ **Specific:** Clear instructions, not vague requests
- ✅ **Reusable:** Applicable to multiple situations with minor customization
- ✅ **Structured:** Template format with placeholders for user context
- ✅ **Tested:** You've used it multiple times with good results
- ✅ **Explained:** Includes "When to use" and "Expected output" sections

**Example prompt contribution:**

```markdown
### [Prompt Name]

**Category:** [Strategic Thinking / Research / Writing / etc.]  
**When to use:** [Specific trigger or situation]  
**Time required:** [Estimate]

**Prompt Template:**
```
[Your prompt with [PLACEHOLDER] for customization]

Context: [USER FILLS IN]
Goal: [USER FILLS IN]
Constraints: [USER FILLS IN]

Help me:
1. [Specific request 1]
2. [Specific request 2]
3. [Specific request 3]
```

**Expected Output:**
[Describe what good output looks like]

**Example Usage:**
[Realistic scenario showing prompt in action]

**Variations:**
- For [specific role]: Adjust [X] 
- For [specific situation]: Add [Y]

**Tips:**
- [Tip that improves results]
- [Common mistake to avoid]
```

---

### Prompt Contribution Process

**Step 1: Validate your prompt**

- Use it at least 5 times in real work
- Verify it works with multiple AI tools (GPT-4, Claude, etc.)
- Refine based on results
- Ensure it's better than generic "help me with X" prompts

**Step 2: Categorize**

Choose category:
- Strategic Thinking
- Research & Analysis
- Writing & Documentation
- Problem-Solving
- Career Development
- Learning & Understanding
- Project Management
- Session Management
- [Suggest new category if needed]

**Step 3: Format properly**

- Use the structure above
- Include realistic example
- Provide usage guidance
- Add tips for better results

**Step 4: Submit**

```bash
# Create branch
git checkout -b prompt/[your-prompt-name]

# Add to Essential_Prompt_Library.md OR create new category
# Update README.md to add prompt to index

# Commit and push
git commit -m "Add [Prompt Name] for [use case]"
git push origin prompt/[your-prompt-name]
```

**Step 5: PR Description**

Include:
- **Category:** Where it fits in library
- **Use case:** Problem it solves
- **Testing:** Results from your usage (success rate, improvements seen)
- **AI compatibility:** Which AI tools you tested with

---

## 📚 Contributing Examples

### Example Case Studies

**We need:**
- Realistic, filled-out examples of templates in use
- Multi-document examples showing integration
- Role-specific examples (marketing, legal, operations, etc.)

**Requirements:**
- Must be **sanitized** (no real names, companies, projects)
- Can be fictional (like Alex Thompson) or anonymized real usage
- Should show realistic detail level (not just minimal placeholders)
- Demonstrate best practices

**Structure:**

Create folder:
```
examples/[role]_[name]/
├── README.md (overview of the example)
├── [Template 1 filled out].md
├── [Template 2 filled out].md
└── [Supporting documents].md
```

See `alex_thompson_data_analyst/` for reference structure.

**Submission process:**
Same as templates - fork, create branch, PR with description.

---

## 📖 Contributing Documentation

### Documentation Needs

**High priority:**
- Video tutorials or walkthroughs
- Quick reference cards (1-page cheat sheets)
- Migration guides (from Notion, Obsidian, etc.)
- Domain-specific guides (ADVISOR for lawyers, engineers, teachers, etc.)
- Troubleshooting common issues

**Medium priority:**
- Improved installation instructions
- Integration guides with popular tools
- Best practices compilations
- FAQ expansions

**Always helpful:**
- Fixing typos
- Clarifying confusing sections
- Adding missing links
- Improving examples

---

### Documentation Style Guide

**Tone:**
- Conversational but professional
- Assume reader is smart but unfamiliar
- Use "you" (not "one should...")
- Active voice preferred

**Structure:**
- Use headings for scanability
- Include code examples where applicable
- Provide before/after comparisons
- Add time estimates for tasks

**Formatting:**
- Use Markdown consistently
- Code blocks with language specification
- Bold for emphasis, not italics
- Use emoji sparingly (only in headings/sections for visual navigation)

---

## 🐛 Reporting Issues

### Before Opening an Issue

1. **Search existing issues** - has this been reported already?
2. **Check documentation** - is it documented but unclear?
3. **Try troubleshooting** - common issues often have known fixes

### Good Issue Reports Include

**For bugs:**
- **What happened:** Describe the problem clearly
- **What you expected:** What should have happened instead
- **Steps to reproduce:** Numbered list so we can verify
- **Environment:** OS, editor, any relevant tools
- **Screenshots:** If applicable

**For feature requests:**
- **Problem statement:** What problem does this solve?
- **Use case:** Real-world scenario where this would help
- **Proposed solution:** Your idea (if you have one)
- **Alternatives considered:** Other approaches you thought about

**For documentation issues:**
- **What's confusing:** Quote the specific section
- **Why it's confusing:** What was unclear or missing
- **Suggested improvement:** How to make it clearer

---

## 🎨 Contributing Integrations

### Tool Integrations

**We welcome:**
- Obsidian plugin or theme for AURELION structure
- VS Code extension for template management
- Notion database templates
- Roam Research integration
- CLI tools for searching/managing templates
- API wrappers for programmatic access

**Requirements:**
- Must be open source (MIT preferred)
- Document how to use it
- Maintain compatibility with core AURELION structure
- Include tests (if code)

**Where to contribute:**
- Small scripts: Add to `/shared/utilities/`
- Full tools: Separate repository, link from ecosystem README
- Extensions: Follow platform guidelines, link from docs

---

## ✅ Pull Request Process

### Before Submitting

- [ ] Test your changes
- [ ] Run spell check
- [ ] Check Markdown formatting (preview in editor)
- [ ] Verify all links work
- [ ] Sanitize any personal/company content
- [ ] Update relevant documentation

### PR Title Format

```
[Type]: Brief description

Types:
- feat: New template, prompt, or feature
- fix: Bug fix or correction
- docs: Documentation improvements
- example: New case study or usage example
- chore: Maintenance (dependencies, formatting, etc.)

Examples:
- feat: Add Meeting Notes Template for recurring standups
- docs: Clarify ADVISOR installation for Windows users
- example: Add marketing manager case study with 5 templates
- fix: Correct broken link in integration guide
```

### PR Description Template

```markdown
## Summary
[2-3 sentences: what you changed and why]

## Type of Change
- [ ] New template
- [ ] New prompt
- [ ] Example/case study
- [ ] Documentation
- [ ] Bug fix
- [ ] Other: [specify]

## Testing
[How did you test this? Who reviewed it?]

## Checklist
- [ ] Sanitized (no personal/company info)
- [ ] FTO-safe (original or public domain content)
- [ ] Tested in real usage (if template/prompt)
- [ ] Documentation updated (if needed)
- [ ] Links verified
- [ ] Spell checked

## Related Issues
Closes #[issue number] (if applicable)
```

---

## 🏛️ Governance & Review

### Review Process

1. **Maintainer review** (1-3 days typical response time)
2. **Feedback or approval**
3. **Revisions** (if needed)
4. **Merge** to main branch
5. **Credit** - you'll be listed in contributors!

### What Gets Merged

**Automatic merge (fast track):**
- Typo fixes
- Broken link fixes
- Minor documentation clarifications

**Standard review:**
- New templates
- New prompts
- Documentation improvements
- Examples

**Extended review:**
- Major structural changes
- New categories or frameworks
- Integration code
- Anything affecting multiple modules

### What Gets Rejected

- Company-proprietary content
- Copyrighted material without permission
- Personal/private information
- Malicious code
- Spam or low-quality contributions
- Contributions that don't fit AURELION philosophy

---

## 🌟 Recognition

### Contributor Credits

All contributors are recognized in:
- Monthly contributor spotlight (coming soon)
- Contributors list in README
- Release notes

### Significant Contributions

Major contributions may receive:
- Co-author credit on significant features
- Featured case study or spotlight
- Early access to new modules (when applicable)
- Community moderator invitation

---

## 📜 Legal

### Licensing

By contributing, you agree:
- Your contribution is your original work or properly licensed
- You grant MIT license to your contribution
- You have authority to make this contribution
- Your contribution doesn't violate any agreements (employer IP, NDAs, etc.)

### Sanitization Responsibility

Contributors are responsible for:
- Removing personal information
- Removing company-specific content
- Verifying FTO compliance
- Not including proprietary methodologies

**When in doubt, open an issue to discuss before contributing.**

---

## 💬 Community Guidelines

### Be Respectful

- Assume good intent
- Provide constructive feedback
- Respect different use cases and workflows
- Remember: there's no "right way" to use AURELION

### Be Helpful

- Answer questions when you can
- Share what worked for youshare what didn't work too)
- Provide context in issues and PRs
- Help newcomers get started

### Be Collaborative

- Credit others' ideas
- Build on existing work thoughtfully
- Communicate early about major changes
- Accept feedback gracefully

---

## 📞 Getting Help

**Questions about contributing?**
- Open a GitHub Discussion
- Tag your question with `question` and `contributing`
- Maintainers typically respond within 2-3 days

**Want to discuss a major contribution before starting?**
- Open an issue with `[RFC]` (Request for Comments) in the title
- Describe your idea
- Get feedback before investing significant time

---

## 🗺️ Roadmap & Priorities

### Current Priorities (Q2 2026)

**High priority contributions:**
- Role-specific examples (marketing, legal, operations, etc.)
- Video tutorials or screencasts
- Integration with popular tools (Obsidian, Notion)
- Prompt refinements based on usage feedback

**Medium priority:**
- Additional templates for specialized use cases
- Documentation translations (internationalization)
- CLI tools or scripts
- Best practices guides

**Lower priority:**
- Aesthetic improvements (unless accessibility-related)
- Advanced features (focus on core usability first)

### Future (Q3-Q4 2026)

- Mobile app or responsive web viewer
- AI-powered prompt suggestions
- Community prompt exchange platform
- Template marketplace (all free, but discoverability)

---

## Thank You! 🙏

Every contribution makes AURELION better for everyone. Whether you fix a typo, share a prompt, or contribute a full case study - thank you for helping build a better knowledge management ecosystem.

**Questions?** Open a GitHub Discussion or Issue.  
**Ideas?** We'd love to hear them - start a Discussion!  
**Ready to contribute?** Fork the repo and get started!

---

**Maintained by:** AURELION Project Team  
**Last Updated:** February 17, 2026  
**Version:** 1.0

---

*Build together, learn together, grow together.*
