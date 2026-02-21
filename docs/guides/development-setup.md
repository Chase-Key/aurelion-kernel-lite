# Development Setup Guide

## Prerequisites

- Git
- VS Code
- GitHub Copilot (optional but recommended)
- PowerShell (Windows) or Bash (Mac/Linux)
- Python 3.9+ (for memory modules)
- Node.js 16+ (optional, for future tools)

## Getting Started

### 1. Clone the Ecosystem

```bash
git clone https://github.com/[your-org]/aurelion-eco.git
cd aurelion-eco
```

### 2. Understand the Structure

```
aurelion-eco/
├── docs/              # All documentation
│   ├── planning/      # Strategy & planning documents
│   ├── architecture/  # Technical design
│   └── guides/        # How-to guides
├── modules/           # All AURELION modules
│   ├── memory/        # Memory management modules
│   ├── kernel/        # Knowledge structure modules
│   ├── nexus/         # Agent orchestration
│   └── sim/           # Testing & simulation
└── shared/            # Shared resources
    ├── templates/     # Reusable templates
    ├── schemas/       # JSON schemas
    └── utilities/     # Shared utilities
```

### 3. Choose Your Module

#### Working on Kernel
```bash
cd modules/kernel/aurelion-kernel-lite
# or
cd modules/kernel/aurelion-kernel-business
```

#### Working on Memory
```bash
cd modules/memory/aurelion-memory-lite
# or
cd modules/memory/aurelion-memory-premium
```

### 4. Install Dependencies

Each module has its own dependencies. See the module's README for specific instructions.

## Development Workflow

### 1. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes
Edit files in your chosen module.

### 3. Test Locally
Each module should have its own test suite.

### 4. Commit
```bash
git add .
git commit -m "Descriptive commit message"
```

### 5. Push & PR
```bash
git push origin feature/your-feature-name
```
Then create a pull request on GitHub.

## Module-Specific Setup

### Kernel Modules
No special setup required—just Markdown files!

1. Navigate to the kernel module
2. Open in VS Code
3. Start editing templates
4. Use GitHub Copilot for suggestions

### Memory Modules

#### Lite Edition
```bash
cd modules/memory/aurelion-memory-lite
pip install -r requirements.txt
python setup.py develop
```

#### Premium Edition
```bash
cd modules/memory/aurelion-memory-premium
pip install -r requirements.txt

# Set up vector DB (choose one)
# For Chroma (local):
pip install chromadb

# For Pinecone (cloud):
pip install pinecone-client
export PINECONE_API_KEY="your-key"
```

#### Business Edition
```bash
cd modules/memory/aurelion-memory-business
pip install -r requirements.txt

# Additional setup for multi-user
# See business edition docs
```

### Nexus Module
```bash
cd modules/nexus/aurelion-nexus
pip install -r requirements.txt
python setup.py develop
```

### Sim Module
```bash
cd modules/sim/aurelion-sim
pip install -r requirements.txt
python setup.py develop
```

## Testing

### Unit Tests
```bash
pytest tests/unit/
```

### Integration Tests
```bash
pytest tests/integration/
```

### End-to-End Tests
```bash
pytest tests/e2e/
```

## Documentation

### Adding Documentation
1. For planning: `docs/planning/`
2. For architecture: `docs/architecture/`
3. For guides: `docs/guides/`
4. For module-specific: `modules/{module}/docs/`

### Documentation Format
- Use Markdown
- Include code examples
- Add diagrams where helpful (ASCII or Mermaid)
- Keep it concise

## Using GitHub Copilot

### Kernel Development
Copilot is especially helpful for:
- Filling out templates
- Creating examples
- Writing documentation
- Generating prompts

### Memory/Code Development
Copilot can help with:
- API implementations
- Test generation
- Error handling
- Documentation

## Common Tasks

### Creating a New Module Variant
1. Copy existing module structure
2. Update naming (follow naming strategy)
3. Modify for tier requirements
4. Update ecosystem README
5. Create module README

### Adding a New Floor to Kernel
1. Create new floor directory: `Floor_0X_Name/`
2. Add templates
3. Update hub index
4. Update README
5. Add Copilot prompts

### Adding Features to Memory
1. Design the feature
2. Write tests first (TDD)
3. Implement feature
4. Update documentation
5. Add examples

## Troubleshooting

### Module Not Found
Ensure you're in the correct directory and have installed dependencies.

### Import Errors
Check your Python path includes the module:
```bash
pip install -e .
```

### Git Issues
Make sure you're on the right branch and have pulled latest changes.

## Best Practices

### Code Style
- Python: Follow PEP 8
- Markdown: Follow CommonMark spec
- YAML: Use 2-space indentation
- JSON: Use 2-space indentation

### Commits
- Use conventional commits format
- Be descriptive
- Reference issues when applicable

### PRs
- Keep PRs focused
- Include tests
- Update documentation
- Request review

### Documentation
- Document as you go
- Include examples
- Update existing docs
- Keep docs close to code

## Getting Help

- **Documentation:** Check `docs/` first
- **Issues:** Search existing GitHub issues
- **Discussions:** Use GitHub Discussions
- **Community:** Join Discord/Slack (when available)

## Resources

- [Architecture Overview](../architecture/)
- [Planning Documents](../planning/)
- [Naming Strategy](../planning/naming-strategy.md)
- [Tiering Strategy](../planning/tiering-strategy.md)
- [Roadmap](../../ROADMAP.md)

---

**Last Updated:** February 16, 2026
