import sqlite3

# Connect to database
conn = sqlite3.connect("data.db")

# Create a cursor
c = conn.cursor()

# Inserting one entry
c.execute("INSERT INTO customers VALUES ('Breno', 'Vieira', 'breno@address.com')")
c.execute("INSERT INTO customers VALUES ('Son', 'Goku', 'goku@tournament.com')")

# Insert multiple entries

customers_values = [
    ("Naruto", "Uzumaki", "naruto@vila.com"),
    ("Midoriya", "Izuku", "midoriya@plusultra.com"),
]

c.executemany("INSERT INTO customers VALUES (?,?,?)", customers_values)

# Commit our commands
conn.commit()

# Close the connection
conn.close()
