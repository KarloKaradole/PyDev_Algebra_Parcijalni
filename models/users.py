import sqlite3

conn = sqlite3.connect('database/user_database.db')
cur = conn.cursor()
conn.commit()

records = cur.fetchall()
cur.close()

print(f"Sadrzaj records objekta: {records}")