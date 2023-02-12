import os
import sqlite3
from typing import List, Tuple


def create_db():
    """Create a database called data.db and customer table"""
    if os.path.exists("data.db"):
        os.remove("data.db")

    conn = sqlite3.connect("data.db")

    c = conn.cursor()

    c.execute(
        """CREATE TABLE customers (
    first_name STRING,
    last_name STRING,

    email STRING
    )"""
    )

    c.execute("INSERT INTO customers VALUES ('Breno', 'Vieira', 'breno@address.com')")
    c.execute("INSERT INTO customers VALUES ('Son', 'Goku', 'goku@tournament.com')")

    customers_values = [
        ("Naruto", "Uzumaki", "naruto@vila.com"),
        ("Midoriya", "Izuku", "midoriya@plusultra.com"),
    ]

    c.executemany("INSERT INTO customers VALUES (?,?,?)", customers_values)

    conn.commit()

    conn.close()


def show_all():
    """Query the DB and return all records"""
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers")

    items = c.fetchall()
    for item in items:
        print(item)

    print("-----------")

    conn.commit()
    conn.close()


def add_record(first: str, last: str, email: str):
    """add a new record on table customers

    Parameters
    ----------
    first : str
        first name
    last : str
        second name
    email : str
        email address
    """
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    conn.commit()
    conn.close()


def del_record(id: int):
    """Delete a record from the table customers using id

    Parameters
    ----------
    id : int
        id to be deleted
    """
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("DELETE from customers WHERE rowid = (?)", id)

    conn.commit()
    conn.close()


def add_many_records(records: List[Tuple]):
    """Add many records on the table customers

    Parameters
    ----------
    records : List[Tuple]
        List with all records
    """
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.executemany("INSERT INTO customers VALUES (?,?,?)", records)

    conn.commit()
    conn.close()


def email_lookup(email: str):
    """Lookup the table customers using email domain

    Parameters
    ----------
    email : str
        email domain
    """
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("SELECT * from customers WHERE email LIKE (?)", (email,))

    items = c.fetchall()

    for item in items:
        print(item)

    print("-----------")
    conn.commit()
    conn.close()
