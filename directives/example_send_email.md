# Send Email

## Goal
Send an email using Gmail API (via MCP) with specified subject, body, and recipient.

## Inputs
- `recipient`: Email address to send to
- `subject`: Email subject line
- `body`: Email body content (plain text or HTML)
- Optional: `cc` - Carbon copy recipients
- Optional: `bcc` - Blind carbon copy recipients

## Tools/Scripts
- MCP Gmail tool: `mcp__gmail__send_email` - Sends email via Gmail API
- Alternative: `execution/send_email.py` - Standalone script for sending emails

## Process
1. Validate inputs (check email format, required fields)
2. Compose email with proper formatting
3. Call Gmail API via MCP or execution script
4. Confirm email was sent successfully
5. Log the result

## Outputs
- Confirmation message with email ID
- Success/failure status

## Edge Cases
- **Invalid email address**: Validate format before sending
- **Gmail API quota exceeded**: Retry with exponential backoff
- **Authentication failure**: Check credentials and token.json
- **Large attachments**: Gmail has 25MB limit per email
- **Rate limiting**: Gmail API has sending limits (default ~100/day for new accounts)

## Notes
- MCP Gmail integration is preferred for email operations
- Gmail API requires OAuth2 authentication (credentials.json and token.json)
- Test emails should go to your own address first
- Always include clear subject lines for tracking
- For bulk emails, consider batch processing with delays
