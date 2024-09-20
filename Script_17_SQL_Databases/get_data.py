import sqlite3

# Establish a connection and create cursor
con = sqlite3.connect('src/database.db')
cur = con.cursor()

# SQL Structure Query Language - Get all rows and all columns by order
cur.execute("SELECT * FROM 'ips' ORDER BY asn")
print('CUR', cur.fetchall())

# Get all rows and certain columns
cur.execute("SELECT address, asn FROM 'ips' ORDER BY asn")
print(cur.fetchall())

# Get all rows where asn is less than 300
cur.execute("SELECT * FROM 'ips' WHERE asn < 300")
print(cur.fetchall())

# Get all rows where asn is 144
cur.execute("SELECT asn FROM 'ips' WHERE asn = 144")
print(cur.fetchall())

# Get all rows where asn is 144
results1 = cur.execute("SELECT * FROM 'ips' WHERE asn < 300 AND domain LIKE '%sa'")
print(results1)

for row in results1:
    print(row)