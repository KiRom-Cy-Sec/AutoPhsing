import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name='phishing.db'):
        self.db_name = db_name
        self.init_db()
    
    def init_db(self):
        """Initialize database with error handling"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS campaigns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    template_name TEXT NOT NULL,
                    target_email TEXT NOT NULL,
                    sender_name TEXT NOT NULL,
                    sent_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    clicked BOOLEAN DEFAULT 0,
                    submitted_data TEXT
                )
            ''')
            
            conn.commit()
            conn.close()
            
        except sqlite3.DatabaseError as e:
            print(f"⚠️  Database error: {e}")
            print("🔄 Creating fresh database...")
            self.create_fresh_db()
    
    def create_fresh_db(self):
        """Create a fresh database file"""
        import os
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE campaigns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                template_name TEXT NOT NULL,
                target_email TEXT NOT NULL,
                sender_name TEXT NOT NULL,
                sent_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                clicked BOOLEAN DEFAULT 0,
                submitted_data TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
        print("✅ Fresh database created")
    
    def add_campaign(self, template, email, sender):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO campaigns (template_name, target_email, sender_name) VALUES (?, ?, ?)',
                      (template, email, sender))
        conn.commit()
        conn.close()
    
    def get_stats(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM campaigns')
        total = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM campaigns WHERE clicked = 1')
        clicks = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM campaigns WHERE submitted_data IS NOT NULL')
        submissions = cursor.fetchone()[0]
        
        conn.close()
        return total, clicks, submissions