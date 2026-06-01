# Directives

This directory contains Layer 1 of the architecture: SOPs (Standard Operating Procedures) written in natural language Markdown.

## Purpose

Directives define:
- **Goals** - What needs to be accomplished
- **Inputs** - What information/data is required
- **Tools** - Which execution scripts to use
- **Outputs** - What the end result should be
- **Edge Cases** - How to handle errors and special scenarios

## Directive Template

Use this template for new directives:

```markdown
# [Directive Name]

## Goal
[What this directive accomplishes]

## Inputs
- Input 1: [description]
- Input 2: [description]

## Tools/Scripts
- `execution/script_name.py` - [what it does]
- `execution/another_script.py` - [what it does]

## Process
1. Step 1: [description]
2. Step 2: [description]
3. Step 3: [description]

## Outputs
- Output 1: [description]
- Output 2: [description]

## Edge Cases
- **Case 1**: [how to handle]
- **Case 2**: [how to handle]

## Notes
- Any additional context
- API limits or constraints
- Timing expectations
```

## Guidelines

1. **Living documents** - Update directives as you learn
2. **Clear and specific** - Write like you're instructing a mid-level employee
3. **Include learnings** - Add API constraints, timing issues, common errors
4. **Reference tools** - Always point to specific execution scripts
5. **No code** - Directives are instructions, not implementation

## Examples

Good directive names:
- `scrape_website.md` - How to scrape a website
- `send_daily_report.md` - Send daily email report
- `update_dashboard.md` - Update Google Sheets dashboard
- `process_leads.md` - Process and organize lead data

## Updating Directives

When you discover something new:
1. Update the relevant directive
2. Add the learning to Edge Cases or Notes
3. Document new API constraints or timing issues
4. Keep the directive accurate and current
