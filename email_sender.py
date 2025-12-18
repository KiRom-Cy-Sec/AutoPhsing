import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SMTP_CONFIG

class EmailSender:
    def __init__(self):
        self.smtp_server = SMTP_CONFIG['server']
        self.smtp_port = SMTP_CONFIG['port']
        self.email = SMTP_CONFIG['email']
        self.password = SMTP_CONFIG['password']
    
    def send_phishing_email(self, target_email, sender_name, template_name, phishing_link):
        try:
            # Read template
            with open(f'templates/{template_name}.html', 'r', encoding='utf-8') as file:
                html_content = file.read()
            
            # Replace placeholders
            html_content = html_content.replace('{{ phishing_link }}', phishing_link)
            html_content = html_content.replace('{{ sender_name }}', sender_name)
            
            # Create message
            msg = MIMEMultipart()
            msg['From'] = f'{sender_name} <{self.email}>'
            msg['To'] = target_email
            msg['Subject'] = self.get_subject(template_name)
            
            msg.attach(MIMEText(html_content, 'html'))
            
            print(f"📧 Attempting to send email via {self.smtp_server}...")
            
            # Send email
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email, self.password)
            server.send_message(msg)
            server.quit()
            
            return True
        except Exception as e:
            print(f"❌ Error sending email: {e}")
            print("\n💡 TROUBLESHOOTING:")
            print("1. Check your email and password in config.py")
            print("2. Make sure you're using an APP PASSWORD, not your regular password")
            print("3. Check if your email provider allows SMTP access")
            print("4. Try enabling 'Less secure app access' if using Gmail")
            return False
    
    def get_subject(self, template_name):
        subjects = {
            'password_reset': 'Urgent: Password Reset Required',
            'invoice_payment': 'Invoice Payment Required - Action Needed', 
            'security_alert': 'Security Alert: Suspicious Login Detected',
            'it_update': 'IT Department: Mandatory System Update'
        }
        return subjects.get(template_name, 'Important Notification')