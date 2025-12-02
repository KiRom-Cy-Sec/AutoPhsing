# Phishing Simulator

A terminal tool to send fake phishing emails for security training.

## ⚠️ WARNING
For educational use only. Only test systems you own or have permission to test.

## Quick Start

1. Edit `config.py` with your email info
2. Run: `python main.py`
3. Follow the menu

## Setup

1. **Edit config.py:**
```python
SMTP_CONFIG = {
    'server': 'smtp.gmail.com',
    'port': 587,
    'email': 'your-email@gmail.com',
    'password': 'your-app-password'

}
```

2. Get App Password (IMPORTANT!)
Don't use your regular Gmail password! You need an "App Password":

Step-by-step for Gmail:
Go to: Google Account Security

Turn on "2-Step Verification" (you might need to sign in)

After 2-Step is on, go back to Security page

Find "App passwords" (under "Signing in to Google")

Select app: Choose "Mail"

Select device: Choose "Other", name it "Phishing Simulator"

Click "Generate" - You'll get a 16-character password

Copy that password into config.py

https://support.google.com/accounts/answer/185833?hl=en

3. Run the program
bash
python main.py
How It Works
Choose from 4 email templates:

Password Reset

Invoice Payment

Security Alert

IT Department Update

Enter the target email and a sender name. The email will be sent.

Troubleshooting
❌ "Password not accepted" error?
You used your regular password, not an App Password

Go back and follow "Get App Password" steps above

Make sure 2-Step Verification is ON

❌ Email not sending?
Check config.py has correct email and app password

Try with a different email provider

Test with your own email first

❌ "Module not found" error?
Make sure all files are in the same folder

You need Python 3.6 or newer
