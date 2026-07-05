import sqlite3
from datetime import datetime


class ChatMemory:

    def __init__(self):
        self.connection = sqlite3.connect("chat_history.db")
        self.cursor = self.connection.cursor()
        self.create_table()


    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            ticker TEXT,
            user_query TEXT,
            price REAL,
            rsi REAL,
            recommendation TEXT,
            report TEXT
        )
        """)
        self.connection.commit()


    def save_chat(
        self,
        ticker,
        query,
        price,
        rsi,
        recommendation,
        report
    ):

        self.cursor.execute("""
        INSERT INTO history(
            timestamp,
            ticker,
            user_query,
            price,
            rsi,
            recommendation,
            report

        )
        VALUES(?,?,?,?,?,?,?)
        """,
        (
            datetime.now().isoformat(),
            ticker,
            query,
            price,
            rsi,
            recommendation,
            report

        ))
        self.connection.commit()


    def get_last_chat(self):
        self.cursor.execute("""
        SELECT *
        FROM history
        ORDER BY id DESC
        LIMIT 1
        """)
        return self.cursor.fetchone()


    def get_company_history(
        self,
        ticker

    ):

        self.cursor.execute("""
        SELECT
        timestamp,
        recommendation,
        report
        FROM history
        WHERE ticker = ?
        ORDER BY id DESC
        """,

        (ticker,))
        return self.cursor.fetchall()


    def close(self):
        self.connection.close()