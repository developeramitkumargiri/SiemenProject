import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT, value INTEGER)")

conn.commit()
conn.close()

print("Database initialized successfully")