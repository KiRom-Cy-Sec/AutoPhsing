#!/usr/bin/env python3
"""
Test script to check if everything is set up correctly
"""

import os
import sys

def check_files():
    """Check if all required files exist"""
    required_files = [
        'main.py',
        'email_sender.py', 
        'config.py',
        'database.py',
        'templates/password_reset.html',
        'templates/invoice_payment.html',
        'templates/security_alert.html',
        'templates/it_update.html'
    ]
    
    print("🔍 Checking project structure...")
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING!")
            missing_files.append(file)
    
    return missing_files

def check_imports():
    """Check if all imports work"""
    print("\n🔍 Checking Python imports...")
    
    try:
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        print("✅ email.mime imports")
    except ImportError as e:
        print(f"❌ email.mime imports: {e}")
        return False
    
    try:
        import smtplib
        print("✅ smtplib import")
    except ImportError as e:
        print(f"❌ smtplib import: {e}")
        return False
    
    try:
        import sqlite3
        print("✅ sqlite3 import")
    except ImportError as e:
        print(f"❌ sqlite3 import: {e}")
        return False
    
    return True

def check_config():
    """Check if config is set up"""
    print("\n🔍 Checking config file...")
    
    try:
        from config import SMTP_CONFIG
        print("✅ Config file structure")
        
        if SMTP_CONFIG['email'] == 'your-email@gmail.com':
            print("❌ Please update your email in config.py")
            return False
        else:
            print(f"✅ Email configured: {SMTP_CONFIG['email']}")
            
        return True
    except Exception as e:
        print(f"❌ Config error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Phishing Simulator - Setup Test")
    print("=" * 40)
    
    # Check files
    missing = check_files()
    if missing:
        print(f"\n❌ Missing files: {missing}")
        sys.exit(1)
    
    # Check imports
    if not check_imports():
        sys.exit(1)
    
    # Check config
    if not check_config():
        print("\n⚠️  Please configure your SMTP settings in config.py")
    
    print("\n🎉 All checks passed! You can now run:")
    print("   python main.py")