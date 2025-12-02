import sqlite3
from datetime import datetime

class Database:
    def __init__(self):
        self.init_db()
    
    def init_db(self):
        conn = sqlite3.connect('phishing.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS campaigns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                template_name TEXT,
                target_email TEXT,
                sender_name TEXT,
                sent_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                clicked BOOLEAN DEFAULT 0,
                submitted_data TEXT
            )
        ''')
        conn.commit()
        conn.close()
    
    def add_campaign(self, template, email, sender):
        conn = sqlite3.connect('phishing.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO campaigns (template_name, target_email, sender_name) VALUES (?, ?, ?)',
                      (template, email, sender))
        conn.commit()
        conn.close()
    
    def get_stats(self):
        conn = sqlite3.connect('phishing.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM campaigns')
        total = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM campaigns WHERE clicked = 1')
        clicks = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM campaigns WHERE submitted_data IS NOT NULL')
        submissions = cursor.fetchone()[0]
        
        conn.close()
        return total, clicks, submissions