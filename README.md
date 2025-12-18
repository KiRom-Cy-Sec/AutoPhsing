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