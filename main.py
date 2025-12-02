from database import Database
from email_sender import EmailSender
import random
import os

class PhishingSimulator:
    def __init__(self):
        self.db = Database()
        self.email_sender = EmailSender()
        self.templates = {
            '1': {'name': 'Password Reset', 'file': 'password_reset'},
            '2': {'name': 'Invoice Payment', 'file': 'invoice_payment'},
            '3': {'name': 'Security Alert', 'file': 'security_alert'},
            '4': {'name': 'IT Department Update', 'file': 'it_update'}
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_banner(self):
        banner = """
╔══════════════════════════════════════════════╗
║           PHISHING SIMULATOR v1.0            ║
║         Educational Purpose Only!            ║
╚══════════════════════════════════════════════╝
        """
        print(banner)

    def show_menu(self):
        print("\n📧 Select Phishing Template:")
        print("1. Password Reset")
        print("2. Invoice Payment")
        print("3. Security Alert")
        print("4. IT Department Update")
        print("5. View Statistics")
        print("6. Exit")

    def get_email_details(self, template_id):
        """Get email and sender name for the selected template"""
        target_email = input("Enter target email address: ").strip()
        sender_name = input("Enter sender name: ").strip()
        return target_email, sender_name

    def send_phishing_email(self, template_id, target_email, sender_name):
        template = self.templates[template_id]

        # Generate fake phishing link (in real scenario, this would be your server)
        campaign_id = random.randint(1000, 9999)
        phishing_link = f"http://fake-phishing-site.com/login?id={campaign_id}"

        print(f"\n🚀 Sending phishing email...")
        print(f"   Template: {template['name']}")
        print(f"   To: {target_email}")
        print(f"   From: {sender_name}")

        success = self.email_sender.send_phishing_email(
            target_email, sender_name, template['file'], phishing_link
        )

        if success:
            print("✅ Email sent successfully!")
            self.db.add_campaign(template['name'], target_email, sender_name)
        else:
            print("❌ Failed to send email. Check SMTP configuration.")

    def show_stats(self):
        total, clicks, submissions = self.db.get_stats()
        print(f"\n📊 Statistics:")
        print(f"   Total Campaigns: {total}")
        print(f"   Total Clicks: {clicks}")
        print(f"   Total Submissions: {submissions}")

        if total > 0:
            click_rate = (clicks / total) * 100
            submission_rate = (submissions / total) * 100
            print(f"   Click Rate: {click_rate:.1f}%")
            print(f"   Submission Rate: {submission_rate:.1f}%")

    def run(self):
        self.clear_screen()
        self.show_banner()

        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-6): ").strip()

            if choice in ['1', '2', '3', '4']:
                # User already selected the template in the main menu
                template_id = choice
                
                # Get email details
                target_email = input("\nEnter target email address: ").strip()
                sender_name = input("Enter sender name: ").strip()
                
                # Send the email
                self.send_phishing_email(template_id, target_email, sender_name)

            elif choice == '5':
                self.show_stats()

            elif choice == '6':
                print("Goodbye!")
                break

            else:
                print("❌ Invalid choice!")

            input("\nPress Enter to continue...")
            self.clear_screen()
            self.show_banner()

if __name__ == "__main__":
    simulator = PhishingSimulator()
    simulator.run()
