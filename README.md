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

### Get App Password (IMPORTANT!)
You can't use your normal Gmail password. You need an "App Password":

1. Go here: https://myaccount.google.com/security
2. Turn ON "2-Step Verification"
3. Go back to Security page
4. Click "App passwords"
5. Select: App → Mail, Device → Other (name it "Phishing Tool")
6. Click Generate
7. Copy the 16-character password into config.py

## How to Add Your Own Templates
### Step 1: Create HTML file
In templates/ folder, create new_template.html:

```html
<!DOCTYPE html>
<html>
<body>
  <h2>Your Subject Here</h2>
  <p>Your email content here.</p>
  <p><a href="{{ phishing_link }}">Click here</a></p>
  <p>- {{ sender_name }}</p>
</body>
</html>
```
### Step 2: Add to main.py
Find this part in main.py:

```python
self.templates = {
    '1': {'name': 'Password Reset', 'file': 'password_reset'},
    '2': {'name': 'Invoice Payment', 'file': 'invoice_payment'},
    '3': {'name': 'Security Alert', 'file': 'security_alert'},
    '4': {'name': 'IT Department Update', 'file': 'it_update'}
}
```
Add your new template:

```python
self.templates = {
    '1': {'name': 'Password Reset', 'file': 'password_reset'},
    '2': {'name': 'Invoice Payment', 'file': 'invoice_payment'},
    '3': {'name': 'Security Alert', 'file': 'security_alert'},
    '4': {'name': 'IT Department Update', 'file': 'it_update'},
    '5': {'name': 'Your Template Name', 'file': 'new_template'}  # ← Added
}
```
### Step 3: Add email subject
In email_sender.py, find get_subject function and add:

```python
def get_subject(self, template_name):
    subjects = {
        'password_reset': 'Urgent: Password Reset Required',
        'invoice_payment': 'Invoice Payment Required',
        'security_alert': 'Security Alert: Suspicious Login',
        'it_update': 'IT Department: System Update',
        'new_template': 'Your Email Subject Here'  # ← Added
    }
    return subjects.get(template_name, 'Important Notification')
```
### Step 4: Update menu display
In main.py, find show_menu function and add option 5:

```python
def show_menu(self):
    print("\n📧 Select Phishing Template:")
    print("1. Password Reset")
    print("2. Invoice Payment")
    print("3. Security Alert")
    print("4. IT Department Update")
    print("5. Your Template Name")  # ← Added
    print("6. View Statistics")
    print("7. Exit")
```

