import sqlite3

# Connect to database
conn = sqlite3.connect("data.db")

# Create a cursor
c = conn.cursor()

# Querying with order by
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
items = c.fetchall()

for item in items:
    print(item)

# Commit our command
conn.commit()

# Close the connection
conn.close()
