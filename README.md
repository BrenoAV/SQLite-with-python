# SQLite with Python

- [SQLite with Python](#sqlite-with-python)
- [BASICS](#basics)
  - [Create a connection](#create-a-connection)
  - [Create a database table](#create-a-database-table)
  - [Insert values](#insert-values)
    - [One entry](#one-entry)
    - [Multiple entries](#multiple-entries)
  - [Querying](#querying)
    - [Order by](#order-by)
    - [Limiting](#limiting)
  - [Primary Key](#primary-key)
  - [Where Clause](#where-clause)
  - [Update Record](#update-record)
  - [Delete record](#delete-record)
  - [Drop Table](#drop-table)
- [REFERENCES](#references)

Simple commands using the language SQL and Python. The video that was based is in the [REFERENCES](#references) session.

# BASICS

## Create a connection

```python
import sqlite3

conn1 = sqlite3.connect(":memory:") # Create in memory
conn2 = sqlite3.connect("data.db")

# Close a connection
conn1.close()
conn2.close()
```

- After doing the operations we need close the connection

## Create a database table

- **[def] Cursor:** it's an object to execute commands on database. For creating a table we need to define a cursor and use the method `execute` which permits executing SQL in python.

```python
c = conn.cursor()
# And now we can create a table
c.execute(
    """CREATE TABLE customers (
    first_name TEXT,
    last_name TEXT,
    email TEXT
    )"""
)
```

- The five types of datatype in SQLite is:
  
| datatype | explanation                                                          |
| -------- | -------------------------------------------------------------------- |
| NULL     | The value is a NULL value                                            |
| INTEGER  | The value is signed integer, and can be stored in until 8 bytes      |
| REAL     | The value is a floating point value (8 bytes)                        |
| TEXT     | The value is a string (UTF-8, UTF-16BE OR UTF-16LE)                  |
| BLOB     | The value is a blob of data, stored exactly as it was input (binary) |

- After create a command, we need to commit it for apply our command in connected database:

```python
# Commit our command
conn.commit()
```

## Insert values

### One entry

```python
c.execute("INSERT INTO custormers VALUES ('First', 'Last', 'email@address.com')")
```

### Multiple entries

- For SQL the symbol `?` is a placeholder

```python
many_entries = [('First1', 'Last1', 'email1@adress.com'), 
                ('First2', 'Last2', 'email2@adress.com')]
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_entries)
```

## Querying

```python
# Querying the database
c.execute("SELECT * FROM customers")
items = c.fetchall()
```

### Order by

- **ASC**ending
- **DESC**ending

```python
# Querying
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
items = c.fetchall()
```

### Limiting

```python
c.execute("SELECT rowid, * FROM customers LIMIT 1")
items = c.fetchall()
```

## Primary Key 

- In SQLite we don't need to create a system to increment the `primary key ID`

```python
# Querying the database
c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
```

## Where Clause

- When we need filter a row to specify search condition

```python
# First querrying
c.execute("SELECT rowid, * FROM customers WHERE last_name = 'Goku'")
items = c.fetchall()

# Second querrying
c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%plusultra.com'")
items = c.fetchall()
```

- You can use comparison operators like: `=`, `>`, `<=`, ...
- You can use logical operators like: `ALL`, `AND`, `LIKE`, `NOT`, ...

More options: [sqlite-where](https://www.sqlitetutorial.net/sqlite-where/)

## Update Record

- For updates, we can use UPDATE and WHERE together

```python

# Update records
c.execute(
    """UPDATE customers SET first_name = 'John'
             WHERE last_name = 'Goku'
"""
)
```

- Or the better approach it's using a *Primary Key ID*

```python
# Update records
c.execute(
    """UPDATE customers SET first_name = 'John'
             WHERE rowid = 2
"""
)
```

## Delete record

```python
# Update records
c.execute("DELETE from customers WHERE rowid = 1")
```

## Drop Table

```python
# Drop Table (delete the table)
c.execute("DROP TABLE customers")
```

# REFERENCES

[SQLite Databases With Python - Full Course](https://www.youtube.com/watch?v=byHcYRpMgI4)
