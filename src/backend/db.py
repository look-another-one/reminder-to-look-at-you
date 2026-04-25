import sqlite3
from pathlib import Path

DB_PATH = "db/data.db"
Path("db").mkdir(parents=True, exist_ok=True)

def init_db():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS screen_time(id INTEGER PRIMARY KEY, date TEXT UNIQUE, screentime_seconds INTEGER)")
    con.commit()
    con.close()

def get_screentime(date_str):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT screentime_seconds FROM screen_time WHERE date = ?", (date_str,))
    result = cur.fetchone()
    con.close()
    return result[0] if result else 0

def update_screentime(date_str, seconds):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    # Insert or update (UPSERT)
    cur.execute("""
        INSERT INTO screen_time (date, screentime_seconds) 
        VALUES(?, ?) 
        ON CONFLICT(date) DO UPDATE SET screentime_seconds = ?
    """, (date_str, seconds, seconds))
    con.commit()
    con.close()


