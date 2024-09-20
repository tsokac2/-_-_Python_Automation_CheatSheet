# Convert data from DB to *.csv
import sqlite3
import pandas

# Establish a connection and create cursor
con = sqlite3.connect('src/database.db')
cur = con.cursor()

df = pandas.read_sql_query("SELECT * FROM 'ips' ORDER BY asn", con)
print(df)

df.to_csv('src/database.csv', index=None)