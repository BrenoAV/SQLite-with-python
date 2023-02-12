import sqlite3

# Creating a connection
# If you want to create a connnection in memory: ":memory:"
conn = sqlite3.connect("data.db")

# Create a cursor
c = conn.cursor()

# Create a table
c.execute(
    """CREATE TABLE customers (
    first_name STRING,
    last_name STRING,

    email STRING
    )"""
)

# Commit our command
conn.commit()

# Close our connection
conn.close()
