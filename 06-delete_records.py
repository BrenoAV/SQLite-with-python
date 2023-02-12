import sqlite3

# Connect to database
conn = sqlite3.connect("data.db")

# Create a cursor
c = conn.cursor()

# Delete records
c.execute("DELETE from customers WHERE rowid = 1")

# Commit our command
conn.commit()

# Close the connection
conn.close()
