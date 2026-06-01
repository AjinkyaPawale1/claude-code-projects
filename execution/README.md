# Execution Scripts

This directory contains Layer 3 of the architecture: deterministic Python scripts that perform reliable, testable operations.

## Purpose

These scripts handle:
- API calls (Gmail, Google Sheets, etc.)
- Data processing and transformation
- File operations
- Database interactions
- Any deterministic operations

## Guidelines

1. **One responsibility per script** - Keep scripts focused
2. **Clear inputs/outputs** - Document what each script expects and returns
3. **Error handling** - Fail gracefully with clear error messages
4. **Environment variables** - Use `.env` for configuration
5. **Testable** - Write scripts that can be tested independently

## Common Patterns

### Reading Environment Variables
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY_NAME')
```

### Error Handling
```python
try:
    result = do_something()
    print(f"Success: {result}")
except Exception as e:
    print(f"Error: {str(e)}")
    exit(1)
```

### CLI Arguments
```python
import argparse

parser = argparse.ArgumentParser(description='Script description')
parser.add_argument('--input', required=True, help='Input file path')
args = parser.parse_args()
```

## Script Naming

Use descriptive, action-oriented names:
- `scrape_single_site.py` - Scrapes one website
- `send_email.py` - Sends an email via Gmail
- `update_sheet.py` - Updates a Google Sheet
- `process_data.py` - Processes data file

## Dependencies

Install required packages:
```bash
pip install python-dotenv google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

Or create a `requirements.txt` and run:
```bash
pip install -r requirements.txt
```
