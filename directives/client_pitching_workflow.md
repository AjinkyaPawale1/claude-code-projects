# Client Pitching Workflow

## Overview
Complete workflow for researching potential clients and generating personalized pitch emails for AI/software engineering services.

## Your Background
- **Name**: Ajinkya Pawale
- **Role**: AI Engineer & Application Engineer
- **Expertise**: AI/ML applications, software development, data engineering, automation
- **Value Proposition**: Custom AI solutions that solve real business problems with measurable ROI

## Complete Workflow

### Step 1: Research Client
**Directive**: [research_client.md](research_client.md)

When you want to pitch a new client, start here:

```
User: "I want to pitch [Company Name]"

Claude: I'll research [Company Name] to identify AI opportunities.
1. Gathers company information
2. Identifies pain points
3. Proposes matching solutions
4. Creates client profile in .tmp/clients/
```

**What Claude does**:
- Web research on the company
- Industry analysis
- Identify specific pain points
- Match pain points to AI/engineering solutions
- Generate client profile JSON

**Output**: `.tmp/clients/[company_name]_profile.json`

---

### Step 2: Generate Pitch Email
**Directive**: [generate_pitch_email.md](generate_pitch_email.md)

After research is complete:

```
User: "Generate a pitch email for [Company Name]"
OR
User: "Generate a pitch email for [Company Name] focusing on automation"

Claude: I'll generate a personalized pitch email.
1. Loads client profile
2. Creates customized email
3. Saves draft for review
```

**Options**:
- **Tone**: professional (default), casual, formal, technical
- **Focus**: Specific solutions (automation, analytics, nlp, computer-vision)

**Output**:
- Email subject line
- Email body
- Draft saved to `.tmp/clients/[company_name]_pitch_email_[timestamp].txt`

---

### Step 3: Review and Send
**Tools**: MCP Gmail or execution/send_email.py

```
User: "Send the pitch email to jane@example.com"

Claude: I'll send the pitch email via Gmail.
1. Reviews the draft
2. Customizes contact name
3. Sends via Gmail API
```

**Before sending**:
- Review email for accuracy
- Customize {contact_name} placeholder
- Verify recipient email
- Check timing (Tuesday-Thursday, 10am-2pm best)

---

## Quick Commands

### Research a new client
> "Research [Company Name] for pitching"
> "I want to pitch [Company Name], please research them"

### Generate pitch email
> "Generate a pitch email for [Company Name]"
> "Create a professional pitch for [Company Name] focusing on automation"
> "Draft a casual pitch email for [Company Name]"

### Send email
> "Send the pitch email to [email@example.com]"
> "Send the draft to [contact_name] at [email]"

### Modify and regenerate
> "Make it more technical"
> "Focus on data analytics instead"
> "Make it shorter"

---

## Solution Categories

### 1. AI/ML Applications
- **LLM Integration**: Chatbots, document processing, content generation
- **Predictive Analytics**: Forecasting, trend analysis, risk assessment
- **NLP**: Sentiment analysis, text classification, information extraction
- **Computer Vision**: Image classification, object detection, OCR

### 2. Automation
- **Workflow Automation**: RPA, process automation, task scheduling
- **Data Pipeline**: ETL, data integration, real-time processing
- **API Integration**: System integration, microservices, webhooks

### 3. Application Development
- **Web Applications**: Full-stack development, dashboards, portals
- **Mobile Apps**: iOS/Android applications
- **Desktop Software**: Cross-platform applications

### 4. Data Engineering
- **Data Infrastructure**: Data warehouses, lakes, pipelines
- **Analytics**: BI dashboards, reporting, visualization
- **Database Optimization**: Performance tuning, schema design

---

## Industry-Specific Pain Points

### E-commerce
- Customer support automation
- Personalization engines
- Inventory forecasting
- Visual search
- Fraud detection

### Healthcare
- Medical record processing
- Appointment scheduling automation
- Diagnostic assistance
- Patient data integration
- Compliance documentation

### Finance
- Fraud detection
- Risk assessment
- Document processing (KYC, loan applications)
- Algorithmic trading
- Customer service automation

### Manufacturing
- Predictive maintenance
- Quality control (computer vision)
- Supply chain optimization
- Production forecasting
- Equipment monitoring

### Real Estate
- Property valuation models
- Document processing (contracts, leases)
- Market analysis
- Lead scoring
- Virtual tours/property visualization

### SaaS/Technology
- Product analytics
- Customer churn prediction
- Feature usage analysis
- Automated testing
- DevOps automation

---

## Email Best Practices

### Do's
✓ Personalize based on research
✓ Reference specific pain points
✓ Focus on business outcomes, not tech features
✓ Keep it under 200 words for cold outreach
✓ One clear call to action
✓ Show you understand their business
✓ Use their language (industry terms)
✓ Quantify value when possible

### Don'ts
✗ Generic "I offer AI services" messages
✗ Talk too much about yourself
✗ Use buzzwords without substance
✗ Multiple CTAs (confusing)
✗ Attachments in cold emails
✗ Long paragraphs (hard to scan)
✗ Aggressive sales language
✗ Promise unrealistic results

---

## Follow-Up Process

### No Response After 3-5 Days
**First Follow-up**:
- Brief reminder
- Add value (share article, case study)
- Restate CTA

### No Response After Another Week
**Second Follow-up**:
- Different angle (new pain point)
- Even shorter
- Breakup email ("Should I close your file?")

### They Respond Positively
- Schedule call quickly
- Prepare demo or case studies
- Come with specific ideas for their business

---

## Success Metrics

Track these for each pitch:
- Open rate (via email tracking tools)
- Response rate
- Calls booked
- Deals closed
- Time from pitch to close

Iterate based on what works:
- Test different subject lines
- Try different tones
- Focus on different pain points
- Adjust email length

---

## Files Created by Workflow

```
.tmp/clients/
├── [company]_profile.json          # Research data
├── [company]_pitch_email_*.txt     # Email drafts
└── client_profile_template.json    # Template for manual profiles
```

---

## Tips for Success

1. **Research Deeply**: Spend 10-15 minutes researching each client
2. **Be Specific**: Generic pitches get ignored
3. **Show Value Fast**: Lead with their pain, not your credentials
4. **Low Friction CTA**: Make it easy to say yes (15-min call)
5. **Timing Matters**: Tuesday-Thursday mornings get best responses
6. **Follow Up**: Most deals happen after follow-ups
7. **Learn and Iterate**: Track what works, double down on it
8. **Personalize at Scale**: Use this system to maintain quality while reaching more prospects

---

## Troubleshooting

### "Not enough information about the company"
- Focus on industry-standard pain points
- Research competitors to infer challenges
- Be upfront: "I noticed X is common in your industry..."

### "Too technical for non-technical audience"
- Use "professional" tone (default)
- Focus on business outcomes, not tech
- Avoid jargon, use plain language

### "Not technical enough for engineering leads"
- Use "technical" tone
- Include more implementation details
- Reference specific technologies

### "Email feels too long"
- Aim for 150-200 words
- Cut credentials section shorter
- Focus on one pain point, one solution

### "Want to pitch multiple solutions"
- Choose 1-2 most impactful
- Mention others briefly in CTA: "...and several other areas"
- Save details for the call
