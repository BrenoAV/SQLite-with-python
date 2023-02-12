import sqlite3

# Connect to database
conn = sqlite3.connect("data.db")

# Create a cursor
c = conn.cursor()

# Update records
c.execute(
    """UPDATE customers SET first_name = 'John'
             WHERE rowid = 2
"""
)


# Commit our command
conn.commit()

# Close the connection
conn.close()
