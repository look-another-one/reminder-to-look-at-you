import sqlite3


con = sqlite3.connect("db/data.db")
cur = con.cursor()

command1 = ("CREATE TABLE IF NOT EXISTS screen_time(id INTEGER PRIMARY KEY, date TEXT, screentime TEXT)")
cur.execute(command1)

command2 = ("INSERT INTO screen_time(date, screentime) VALUES(?, ?)")
cur.execute(command2, (datetime.now(), "10:00"))

con.commit()
con.close()

