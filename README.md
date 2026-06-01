# Claude Code Workspace

This workspace follows the 3-layer architecture defined in [CLAUDE.md](CLAUDE.md).

## 🚀 Client Pitching System

**NEW!** Complete workflow for pitching AI/software engineering services to potential clients.

- **Quick Start**: [PITCHING_QUICKSTART.md](PITCHING_QUICKSTART.md)
- **Full Overview**: [PITCHING_SYSTEM_SUMMARY.md](PITCHING_SYSTEM_SUMMARY.md)
- **Workflow Details**: [directives/client_pitching_workflow.md](directives/client_pitching_workflow.md)

**How to use**: Just say *"I want to pitch [Company Name]"* and Claude will:
1. Research the company
2. Identify AI opportunities
3. Generate a personalized pitch email
4. Send it when you're ready

## Directory Structure

```
.
├── CLAUDE.md           # Main architecture and operating principles
├── directives/         # Layer 1: SOPs in Markdown (what to do)
├── execution/          # Layer 3: Python scripts (doing the work)
├── .tmp/               # Temporary/intermediate files (regenerated, not committed)
├── MCP Gmail/          # Gmail integration via MCP
├── .env                # Environment variables (not committed)
├── .env.example        # Template for environment variables
└── credentials.json    # Google OAuth credentials (not committed)
```

## Quick Start

1. **Copy environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Fill in your API keys and credentials in `.env`**

3. **Add your Google OAuth credentials** (if using Google APIs):
   - Place `credentials.json` in the root directory
   - Run initial auth to generate `token.json`

## Architecture Overview

### Layer 1: Directives (`directives/`)
Natural language SOPs that define:
- Goals and objectives
- Required inputs
- Tools/scripts to use
- Expected outputs
- Edge cases and error handling

### Layer 2: Orchestration (AI Agent)
The AI agent (Claude) handles:
- Reading and interpreting directives
- Intelligent routing and decision making
- Calling execution tools in the right order
- Error handling and recovery
- Updating directives with learnings

### Layer 3: Execution (`execution/`)
Deterministic Python scripts that:
- Handle API calls
- Process data
- Perform file operations
- Interact with databases
- Execute reliable, testable operations

## Key Principles

1. **Check for tools first** - Before creating new scripts, check if tools exist in `execution/`
2. **Self-anneal when things break** - Fix errors, update scripts, document learnings
3. **Update directives** - Keep directives current with new constraints and approaches
4. **Cloud deliverables** - Final outputs go to Google Sheets/Slides/etc., not local files
5. **Temporary intermediates** - All processing files go in `.tmp/` and can be regenerated

## File Organization

- **Deliverables**: Google Sheets, Slides, or other cloud services
- **Intermediates**: `.tmp/` directory (temporary, regenerated)
- **Scripts**: `execution/` directory (deterministic tools)
- **Instructions**: `directives/` directory (SOPs)

## Self-Annealing Loop

When errors occur:
1. Fix the issue
2. Update the tool
3. Test the tool
4. Update the directive with new learnings
5. System is now stronger

## Modal Webhooks (Optional)

For event-driven execution, webhooks can be set up using Modal. See `directives/add_webhook.md` for complete setup instructions.

## Notes

- Everything in `.tmp/` can be safely deleted and regenerated
- Never commit `.env`, `token.json`, or `credentials.json`
- Directives are living documents - update them as you learn
- Use deterministic scripts instead of manual work to ensure reliability
