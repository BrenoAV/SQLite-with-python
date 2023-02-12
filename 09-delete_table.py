import sqlite3

# Connect to database
conn = sqlite3.connect("data.db")

# Create a cursor
c = conn.cursor()

# Drop Table (delete the table)
c.execute("DROP TABLE customers")

# Commit our command
conn.commit()

# Close the connection
conn.close()
