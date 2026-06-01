# Client Pitching System

## Overview
A complete workflow for researching potential clients and generating personalized AI/software engineering service pitch emails.

## System Components

### Directives (Layer 1)
1. **[research_client.md](research_client.md)** - Research companies and identify opportunities
2. **[generate_pitch_email.md](generate_pitch_email.md)** - Generate personalized pitch emails
3. **[client_pitching_workflow.md](client_pitching_workflow.md)** - Complete workflow guide

### Execution Scripts (Layer 3)
1. **[../execution/generate_pitch_email.py](../execution/generate_pitch_email.py)** - Email generation script

### Templates
1. **[../.tmp/clients/client_profile_template.json](../.tmp/clients/client_profile_template.json)** - Client profile structure

## How It Works

### User Request
> "I want to pitch Acme Corporation"

### Claude's Process

1. **Research Phase** (follows research_client.md)
   - Gathers company information
   - Identifies industry and pain points
   - Proposes matching AI/software solutions
   - Creates client profile JSON

2. **Generation Phase** (follows generate_pitch_email.md)
   - Loads client profile
   - Generates personalized email
   - Customizes tone and focus
   - Saves draft for review

3. **Send Phase** (uses send_email.py or MCP Gmail)
   - Reviews final draft
   - Sends via Gmail API
   - Tracks sent emails

## File Organization

```
.tmp/clients/
├── client_profile_template.json          # Template structure
├── acme_corporation_profile.json         # Research data
├── acme_corporation_pitch_email_*.txt    # Email drafts
└── [more client files]
```

## Customization

### Email Tones
- **professional**: Default, balanced approach
- **casual**: Friendly, conversational
- **formal**: Traditional, detailed
- **technical**: Engineering-focused

### Focus Areas
- automation
- data-analytics
- nlp (chatbots, text processing)
- computer-vision
- predictive-models

### Example Commands
```
"Generate a technical pitch for Acme Corp"
"Generate a casual pitch focusing on automation"
"Make it more formal and focus on data analytics"
```

## Your Background (What Gets Pitched)

**Name**: Ajinkya Pawale
**Title**: AI Engineer & Application Engineer

**Expertise**:
- AI/ML: LLMs, NLP, Computer Vision, Predictive Analytics
- Software Engineering: Full-stack development, APIs, system integration
- Data Engineering: Pipelines, analytics, data infrastructure
- Automation: Workflow automation, RPA, process optimization

**Value Proposition**:
Custom AI solutions that solve real business problems with measurable ROI

## Workflow States

### 1. Pre-Research
- User identifies target company
- Optional: User provides context

### 2. Research
- Company info gathered
- Pain points identified
- Solutions proposed
- Profile saved

### 3. Email Generation
- Profile loaded
- Email customized
- Draft created
- Ready for review

### 4. Review & Send
- User reviews draft
- Adjustments made if needed
- Email sent via Gmail
- Track response

### 5. Follow-up
- No response after 3-5 days: First follow-up
- Still no response: Second follow-up
- Response received: Schedule call

## Best Practices

### Research
✓ Spend 10-15 minutes per client
✓ Look for specific pain points
✓ Reference recent news/events
✓ Understand their tech stack
✓ Check competitors

### Email Content
✓ Personalize based on research
✓ Lead with their pain, not your credentials
✓ Keep under 200 words
✓ One clear CTA
✓ Quantify value when possible
✓ Show you understand their business

### Timing
✓ Send Tuesday-Thursday
✓ 10am-2pm local time
✓ Follow up after 3-5 days
✓ Second follow-up after another week

### Avoid
✗ Generic "AI services" messages
✗ Buzzwords without substance
✗ Multiple CTAs
✗ Long paragraphs
✗ Attachments in cold emails

## Success Metrics

Track for each pitch:
- Email sent date
- Open (if tracking enabled)
- Response received
- Call scheduled
- Deal status

Iterate based on results:
- Test subject lines
- Try different tones
- Adjust focus areas
- Optimize length

## Troubleshooting

### Limited Company Information
→ Focus on industry-standard pain points
→ Research competitors to infer challenges
→ Be transparent: "I noticed X is common in your industry..."

### Wrong Tone for Audience
→ Use "professional" for mixed audiences
→ Use "technical" for engineering leads
→ Use "casual" for startups
→ Use "formal" for enterprise/traditional

### Email Too Long
→ Cut credentials section
→ Focus on one pain point
→ Remove extra solutions
→ Aim for 150-200 words

### Multiple Solutions to Pitch
→ Choose 1-2 most impactful
→ Mention others in CTA
→ Save details for the call

## Self-Annealing

As you use this system:
1. Track what works (response rates, calls booked)
2. Update directives with learnings
3. Refine email templates
4. Add industry-specific insights
5. Improve pain point identification

## Quick Reference

| Command | Action |
|---------|--------|
| "I want to pitch [Company]" | Start full workflow |
| "Research [Company]" | Research only |
| "Generate pitch for [Company]" | Email generation only |
| "Make it more [tone]" | Adjust tone |
| "Focus on [area]" | Change focus area |
| "Send to [email]" | Send final email |

## Related Files

- [PITCHING_QUICKSTART.md](../PITCHING_QUICKSTART.md) - Quick start guide
- [client_pitching_workflow.md](client_pitching_workflow.md) - Detailed workflow
- [research_client.md](research_client.md) - Research directive
- [generate_pitch_email.md](generate_pitch_email.md) - Email generation directive
