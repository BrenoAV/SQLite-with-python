import sqlite3

# Connect to database
conn = sqlite3.connect("data.db")

# Create a cursor
c = conn.cursor()

# Querying
print("First Querrying")
c.execute("SELECT rowid, * FROM customers WHERE last_name = 'Goku'")
items = c.fetchall()
for item in items:
    print(item)

print("Second Querrying")
c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%plusultra.com'")
items = c.fetchall()
for item in items:
    print(item)

# Commit our command
conn.commit()

# Close the connection
conn.close()
