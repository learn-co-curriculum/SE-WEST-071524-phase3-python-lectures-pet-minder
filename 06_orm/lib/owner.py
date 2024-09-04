# Stretch Goal: Build Out Corresponding Owner Class Methods

# Owner Attributes:
# name: string
# phone: string
# email: string
# address: string

import sqlite3

CONN = sqlite3.connect("lib/resources.db")
CURSOR = CONN.cursor()


class Owner:

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS owners(
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone TEXT,
                email TEXT
                address TEXT
            )
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS owners;
        """
        CURSOR.execute(sql)

    def __init__(self, name, phone, email, address, id=None):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def save(self):
        sql = """
            INSERT INTO owners (name, phone, email, address)
            VALUES (?, ?, ?, ?);
        """
        CURSOR.execute(sql, (self.name, self.phone, self.email, self.address))
        CONN.commit()
        self.id = CURSOR.lastrowid
        return self

    def __repr__(self):
        return f"<Owner {self.id}: {self.name}>"
