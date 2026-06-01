#!/usr/bin/env python3
"""
Send Email Script
Sends an email using Gmail API

Usage:
    python send_email.py --to recipient@example.com --subject "Subject" --body "Email body"
"""

import os
import argparse
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_gmail_service():
    """Authenticate and return Gmail API service"""
    creds = None
    token_path = 'token.json'
    creds_path = 'credentials.json'

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(creds_path):
                raise FileNotFoundError(f"Credentials file not found: {creds_path}")
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def create_message(to, subject, body, cc=None, bcc=None):
    """Create email message"""
    message = MIMEText(body)
    message['to'] = to
    message['subject'] = subject
    if cc:
        message['cc'] = cc
    if bcc:
        message['bcc'] = bcc

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

def send_email(to, subject, body, cc=None, bcc=None):
    """Send email via Gmail API"""
    try:
        service = get_gmail_service()
        message = create_message(to, subject, body, cc, bcc)
        sent_message = service.users().messages().send(userId='me', body=message).execute()

        print(f"✓ Email sent successfully!")
        print(f"  Message ID: {sent_message['id']}")
        print(f"  To: {to}")
        print(f"  Subject: {subject}")
        return sent_message

    except Exception as e:
        print(f"✗ Error sending email: {str(e)}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Send email via Gmail API')
    parser.add_argument('--to', required=True, help='Recipient email address')
    parser.add_argument('--subject', required=True, help='Email subject')
    parser.add_argument('--body', required=True, help='Email body content')
    parser.add_argument('--cc', help='CC recipients (comma-separated)')
    parser.add_argument('--bcc', help='BCC recipients (comma-separated)')

    args = parser.parse_args()

    send_email(
        to=args.to,
        subject=args.subject,
        body=args.body,
        cc=args.cc,
        bcc=args.bcc
    )

if __name__ == '__main__':
    main()
