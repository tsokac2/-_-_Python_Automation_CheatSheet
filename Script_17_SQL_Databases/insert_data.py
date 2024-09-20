# Insert data to DB
import sqlite3

# Establish a connection and create cursor
con = sqlite3.connect('src/database.db')
cur = con.cursor()

new_rows = [
    ('100.100.100.100', 'a.b.c', 100),
    ('200.200.200.200', 'f.d.e', 200)
]

cur.executemany("INSERT INTO 'ips' VALUES(?,?,?)", new_rows)
con.commit()

cur.execute("SELECT * FROM 'ips'")
print(cur.fetchall())