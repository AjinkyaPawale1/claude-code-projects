# Research Client

## Goal
Research a potential client company to identify AI/software engineering opportunities, pain points, and areas where custom solutions could add value.

## Inputs
- `company_name`: Name of the target company
- `company_website`: (Optional) Company website URL
- `industry`: (Optional) Industry/sector
- `contact_name`: (Optional) Name of decision maker
- `contact_role`: (Optional) Title/role of contact person

## Tools/Scripts
- `execution/research_client.py` - Gathers company information and identifies opportunities
- Web search for company information
- Industry analysis for common pain points

## Process
1. **Gather Basic Information**
   - Company size, industry, location
   - Products/services they offer
   - Recent news, funding, expansions
   - Technology stack (if publicly available)

2. **Identify Potential Pain Points**
   - Manual processes that could be automated
   - Data they're not leveraging
   - Customer experience gaps
   - Operational inefficiencies
   - Scaling challenges

3. **Match to AI/Engineering Solutions**
   - AI/ML applications (predictive analytics, NLP, computer vision)
   - Automation opportunities
   - Data pipeline improvements
   - Application development/modernization
   - Integration with existing systems

4. **Competitive Analysis**
   - What competitors are doing with AI
   - Industry standards for technology adoption
   - Innovation opportunities

5. **Generate Client Profile**
   - Save research to `.tmp/clients/[company_name]_profile.json`
   - Include: company info, pain points, proposed solutions, talking points

## Outputs
- Client profile JSON saved to `.tmp/clients/`
- Summary of key opportunities
- List of potential solutions to pitch
- Relevant case studies or examples

## Edge Cases
- **Limited public information**: Focus on industry-standard pain points
- **Highly technical company**: Emphasize advanced AI capabilities (LLMs, deep learning, etc.)
- **Non-technical company**: Focus on business outcomes, ROI, ease of use
- **Startup vs Enterprise**: Adjust tone and solution complexity accordingly
- **Privacy-conscious industries** (healthcare, finance): Emphasize security, compliance

## Notes
- Research should take 10-15 minutes per client
- Save all research for future reference
- Update profiles if you learn more about the client
- Look for recent pain points (hiring for specific roles, press releases about challenges)
- Check LinkedIn for company updates and employee posts about challenges
- Industry-specific pain points:
  - **E-commerce**: Personalization, inventory forecasting, customer service automation
  - **Healthcare**: Data integration, predictive diagnostics, administrative automation
  - **Finance**: Fraud detection, risk assessment, document processing
  - **Manufacturing**: Predictive maintenance, quality control, supply chain optimization
  - **Retail**: Customer analytics, demand forecasting, visual search
  - **Real Estate**: Property valuation, document processing, market analysis
