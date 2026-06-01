# Generate Pitch Email

## Goal
Generate a personalized, professional pitch email to a potential client that highlights their pain points and proposes AI/software engineering solutions.

## Inputs
- `client_profile`: Client research data (from research_client directive)
- `sender_name`: Your name (default: Ajinkya Pawale)
- `sender_title`: Your title (default: Senior Technology Consultant, EY)
- `sender_email`: Your email (default: pawaleajinkya7@gmail.com)
- `sender_background`: Your actual experience/resume data
- `tone`: Email tone (default: professional, options: casual, formal, technical)
- `focus_areas`: Specific solutions to emphasize (optional)

## Tools/Scripts
- `execution/generate_pitch_email.py` - Generates personalized pitch email
- Client profile from `.tmp/clients/[company_name]_profile.json`

## Process
1. **Load Client Profile**
   - Read saved research from `.tmp/clients/`
   - Extract key pain points and opportunities

2. **Structure Email**
   - Subject Line: Compelling, specific to their business
   - Opening: Personal, shows research
   - Pain Point: Identify 1-2 specific challenges
   - Solution Overview: How AI/engineering can help
   - Value Proposition: Benefits, ROI, outcomes
   - Credentials: Brief background without being salesy
   - Call to Action: Low-commitment next step
   - Signature: Professional closing

3. **Personalization Elements**
   - Reference recent company news/achievements
   - Industry-specific language
   - Relevant case studies or examples
   - Specific technical solutions (not generic "AI")

**CRITICAL - Authenticity Requirements:**

4. **Verify Against Resume/Background**
   - NEVER claim domain expertise you don't have
   - NEVER fabricate case studies or experience
   - NEVER promise specific ROI without context
   - ALWAYS base credentials on actual resume
   - ALWAYS be transparent about domain differences
   - ALWAYS emphasize transferable technical skills

5. **Honest Positioning Approach**
   - Lead with real experience from actual background
   - Acknowledge domain differences explicitly
   - Position as "technical capabilities that could transfer"
   - Use phrases like:
     - "In my previous role at [Company], I built..."
     - "While my domain was [X], not [Y]..."
     - "I don't have [industry] experience, but..."
     - "The technical fundamentals transfer well..."
     - "I'm genuinely curious about applying these skills to [industry]"
   - Show intellectual honesty as a differentiator

4. **Tone Adjustments**
   - **Professional** (default): Balanced, credible, outcome-focused
   - **Casual**: Friendly, conversational, approachable
   - **Formal**: Traditional, highly professional, detailed
   - **Technical**: Engineering-focused, technical depth, for technical audiences

5. **Generate Email**
   - Create email draft with all components
   - Save to `.tmp/clients/[company_name]_pitch_email.txt`
   - Also prepare Gmail-ready format

## Outputs
- Email subject line
- Email body (plain text and HTML versions)
- Draft saved to `.tmp/clients/` for review
- Ready to send via MCP Gmail or copy-paste

## Edge Cases
- **No prior research**: Prompt to run research_client first
- **Multiple solutions**: Focus on 1-2 most impactful (avoid overwhelming)
- **Cold outreach**: Softer approach, more value-focused
- **Warm introduction**: Can be more direct, reference mutual connection
- **Follow-up**: Shorter, reference previous conversation
- **C-level executives**: Brief, ROI-focused, respect their time
- **Technical leads**: Can include more technical details

## Email Template Structure

### Subject Line Examples
- "Quick question about [specific process] at [Company]"
- "AI solution for [specific pain point] at [Company]"
- "Helping [Company] [achieve specific outcome]"
- "[Mutual connection] suggested I reach out"

### Opening (Personalized)
- Reference recent company news, funding, or achievement
- Show you understand their business
- Establish credibility quickly

### Problem/Opportunity (2-3 sentences)
- Specific pain point from research
- Industry context if relevant
- Current state vs. desired state

### Solution (2-3 sentences)
- Specific AI/engineering solution
- How it addresses their pain point
- Technical approach (brief, not overwhelming)

### Value Proposition (2-3 bullet points)
- Business outcomes (increased revenue, reduced costs, improved efficiency)
- Quantifiable impact if possible
- Competitive advantage

### Credentials (1-2 sentences)
**CRITICAL:** Only include credentials from actual resume/background
- Real projects from actual experience (cite specific companies/roles)
- Transferable technical skills, not fabricated domain expertise
- Acknowledge domain gaps honestly
- Example: "In my previous role as AI Engineer at Elevance Health, I built [specific real project]"
- NOT: "I specialize in aerospace manufacturing" (unless true)

### Call to Action (1 sentence)
- 15-minute call to discuss
- Share a case study or demo
- Answer any questions
- Low-commitment, easy to say yes

### Signature
- Professional sign-off
- Contact information
- LinkedIn profile link

## Notes
- Keep email under 200 words for cold outreach
- Can be longer (250-300) for warm introductions
- Always personalize - no generic templates
- Focus on THEM, not you (avoid "I/we", use "you/your")
- One clear CTA, not multiple options
- Subject line is crucial - spend time on it
- Avoid:
  - Buzzwords without substance ("synergy", "disrupt", "revolutionary")
  - Generic "AI solutions" - be specific
  - Talking too much about yourself
  - Multiple requests in one email
  - Attachments in cold emails (flag for spam)
  - **CRITICAL - NEVER DO:**
    - Claim domain expertise you don't have
    - Fabricate case studies or client work
    - Promise specific ROI without supporting data
    - Pretend to have worked in industries you haven't
    - Use phrases like "I specialize in [industry]" unless 100% true
- Best practices:
  - Send Tuesday-Thursday, 10am-2pm local time
  - Follow up after 3-5 business days if no response
  - A/B test subject lines
  - Keep sentences short and scannable
  - Use whitespace effectively
  - **Authenticity > Sales pitch** - Honesty builds more trust than overselling
  - Position as "curious technical expert" not "domain specialist"
  - Acknowledge gaps, emphasize transferable skills
  - Use real project examples from actual background

---

## CRITICAL: Authenticity & Resume Verification Protocol

**Before generating ANY pitch email, you MUST:**

### Step 1: Verify Background
- Check sender's actual resume/background data
- Identify real projects, companies, and domains worked in
- Note what domains/industries sender has NOT worked in

### Step 2: Match Solutions to Real Experience
- Only cite projects that actually exist in resume
- Use specific company names, technologies, and outcomes from real experience
- Example (GOOD): "In my role as AI Engineer at Elevance Health, I built a multi-agent GPT-4 system..."
- Example (BAD): "I've worked with aerospace manufacturers to implement quality systems..." (if not true)

### Step 3: Honest Domain Positioning
When pitching to industries sender hasn't worked in:
- **Acknowledge the gap explicitly:** "While my background is in [actual domain], not [target domain]..."
- **Emphasize transferable skills:** "The technical fundamentals (computer vision, ML pipelines) transfer well..."
- **Position as curious expert:** "I'm genuinely curious about applying these capabilities to [target industry]"
- **Invite collaboration:** "I'd love to learn about your challenges and explore whether there's fit"

### Step 4: Real Credentials Only
Use this format:
```
Current Role: [Actual current position]
Previous Experience: [Real companies and roles]
Real Projects:
  - [Specific project 1 from resume]
  - [Specific project 2 from resume]
  - [Specific project 3 from resume]
Technical Skills: [Actual skills from resume]
Domains Worked In: [Real domains only]
```

### Example: Honest Pitch to New Domain

**Scenario:** AI Engineer with healthcare background pitching to manufacturing

**WRONG Approach:**
> "I specialize in aerospace manufacturing quality systems and have helped manufacturers implement AI quality inspection..."

**RIGHT Approach:**
> "In my previous role as an AI Engineer at Elevance Health, I built computer vision systems for automated compliance checking - reduced manual review time by 80%. While my domain was healthcare documentation, not manufacturing, the technical fundamentals (computer vision, ML validation, production systems) seem transferable. I'm genuinely curious about whether these capabilities could apply to manufacturing quality assurance. I don't have manufacturing experience, but I do have strong technical skills and intellectual curiosity."

### Why This Works Better:
1. **Builds Trust** - Honesty stands out, especially in cold outreach
2. **Shows Maturity** - Acknowledging gaps = professional credibility
3. **Proves Capability** - Real projects > fabricated claims
4. **Differentiates** - Most vendors oversell; authenticity is rare
5. **Invites Dialogue** - "Let's explore together" > "Buy my solution"

### Sender Default Information:
- **Name:** Ajinkya Pawale
- **Title for Outreach:** AI/ML Engineering Consultant (independent, NOT representing EY)
- **Background:** Previous AI Engineer, Elevance Health (2023-2025)
- **Email:** pawaleajinkya7@gmail.com
- **Phone:** 763-306-4790
- **LinkedIn:** linkedin.com/in/ajinkya-pawale
- **IMPORTANT:** Do NOT mention EY in signature - reaching out as independent consultant
- **Domains Worked:** Healthcare (inpatient claims, call centers), E-commerce
- **Does NOT Have Experience In:** Aerospace, Manufacturing, Finance, Real Estate (unless stated in resume)

**Real Projects to Reference:**
- Multi-agent GPT-4 document compliance system (80% time reduction)
- GenAI call summarization (350+ agents, 55% faster response)
- RAG pipelines for customer context retrieval
- Production ML pipelines in Airflow (4 hours saved per run)
- Kinesis real-time data processing (40% speed improvement)
- Data validation & drift detection systems
- Datadog/Splunk monitoring (20+ dashboards)
- Computer vision agents for image analysis

**Technical Stack (Actual):**
- Languages: Python, PySpark, R, SQL
- ML/AI: PyTorch, TensorFlow, Hugging Face, GPT-4, Langchain
- Computer Vision: CNNs, image analysis
- Data: Pandas, NumPy, scikit-learn
- Cloud: AWS (S3, EC2, Lambda, Kinesis, etc.)
- DevOps: Docker, Git, Airflow, FastAPI

### Self-Check Before Sending:
- [ ] All projects cited exist in sender's actual resume?
- [ ] No fabricated domain expertise?
- [ ] Domain gaps acknowledged honestly?
- [ ] Transferable skills emphasized?
- [ ] Tone is "curious expert" not "domain specialist"?
- [ ] Contact info correct (EY role, correct email)?
- [ ] Real company names used (Elevance Health, not generic)?

If ANY check fails, revise the email to be truthful.
