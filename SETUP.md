# Workspace Setup Guide

Follow these steps to get your workspace fully configured according to the CLAUDE.md architecture.

## Initial Setup

### 1. Install Python Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your actual values
nano .env  # or use your preferred editor
```

### 3. Set Up Google API Credentials

If you're using Gmail or Google Sheets:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select existing)
3. Enable Gmail API and/or Google Sheets API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download credentials and save as `credentials.json` in the project root
6. Run any script that uses Google APIs to generate `token.json`:
   ```bash
   python execution/send_email.py --to test@example.com --subject "Test" --body "Test"
   ```

### 4. Verify MCP Gmail Setup

The MCP Gmail integration is already in the `MCP Gmail/` directory. Verify it's working:

```bash
cd "MCP Gmail/mcp-gmail"
python scripts/test_gmail_setup.py
```

## Directory Structure

After setup, your workspace should look like this:

```
.
├── .env                    # Your environment variables (not committed)
├── .env.example            # Template for environment variables
├── .gitignore              # Git ignore rules
├── .tmp/                   # Temporary files (not committed)
├── CLAUDE.md               # Architecture principles
├── README.md               # Workspace overview
├── SETUP.md                # This file
├── requirements.txt        # Python dependencies
│
├── directives/             # Layer 1: What to do
│   ├── README.md
│   └── example_send_email.md
│
├── execution/              # Layer 3: How to do it
│   ├── README.md
│   └── send_email.py
│
├── MCP Gmail/              # Gmail integration
│   └── mcp-gmail/
│
├── credentials.json        # Google OAuth (not committed)
└── token.json              # Google OAuth token (not committed)
```

## Testing Your Setup

### Test 1: Environment Variables
```bash
# Check if .env is loaded
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('✓ dotenv working')"
```

### Test 2: Google APIs
```bash
# Test Gmail API (sends test email to yourself)
python execution/send_email.py --to your-email@example.com --subject "Test" --body "Testing workspace setup"
```

### Test 3: MCP Gmail
Use the MCP Gmail tools via Claude Code to send a test email.

## Common Issues

### Issue: `ModuleNotFoundError`
**Solution**: Make sure you've installed dependencies:
```bash
pip install -r requirements.txt
```

### Issue: `FileNotFoundError: credentials.json`
**Solution**: Download OAuth credentials from Google Cloud Console and save as `credentials.json` in the project root.

### Issue: Gmail API authentication fails
**Solution**:
1. Delete `token.json` if it exists
2. Run the script again to re-authenticate
3. Make sure you're using the correct Google account

### Issue: Permission denied when running Python scripts
**Solution**: Make scripts executable:
```bash
chmod +x execution/*.py
```

## Next Steps

1. **Create your first directive**: Copy `directives/example_send_email.md` as a template
2. **Write execution scripts**: Add Python scripts to `execution/` for deterministic operations
3. **Test the system**: Try the self-annealing loop by intentionally breaking something and fixing it
4. **Update directives**: As you learn, keep your directives current

## Optional: Modal Webhooks

For event-driven execution, you can set up Modal webhooks:

1. Install Modal: `pip install modal`
2. Create Modal account: `modal setup`
3. See `directives/add_webhook.md` for complete webhook setup (create this directive when needed)

## Getting Help

- Read [CLAUDE.md](CLAUDE.md) for architecture principles
- Check [README.md](README.md) for workspace overview
- Review example directive: [directives/example_send_email.md](directives/example_send_email.md)
- Review example script: [execution/send_email.py](execution/send_email.py)

## Maintenance

### Keep dependencies updated
```bash
pip list --outdated
pip install --upgrade package-name
pip freeze > requirements.txt
```

### Clean temporary files
```bash
rm -rf .tmp/*
```

### Backup important files
Never commit but keep backed up elsewhere:
- `.env`
- `credentials.json`
- `token.json`
