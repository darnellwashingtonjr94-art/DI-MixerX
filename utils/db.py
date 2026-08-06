import sqlite3
import os

class TrapDatabase:
    def __init__(self, db_path="data/trap_ledger.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._create_tables()

    def _create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attackers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                ip_address TEXT,
                user_agent TEXT,
                captured_credentials TEXT,
                request_path TEXT
            )
        ''')
        self.conn.commit()

    def log_attack(self, ip, user_agent, credentials, path):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO attackers (ip_address, user_agent, captured_credentials, request_path)
            VALUES (?, ?, ?, ?)
        ''', (ip, user_agent, credentials, path))
        self.conn.commit()
