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
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS owners;
        """
        CURSOR.execute(sql)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS owners
                (id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                phone INTEGER,
                address TEXT);
        """
        CURSOR.execute(sql)

    def __init__(self, name, email, phone, address, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def save(self):
        sql = """
            INSERT INTO owners (name, email, phone, address)
            VALUES (?, ?, ?, ?);
        """
        CURSOR.execute(
            sql,
            (
                self.name,
                self.email,
                self.phone,
                self.address,
            ),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
