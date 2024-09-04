import sqlite3

CONN = sqlite3.connect("lib/resources.db")
CURSOR = CONN.cursor()


class Handler:

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS handlers
                (id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                phone TEXT,
                hourly_rate FLOAT);
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS handlers;
        """
        CURSOR.execute(sql)

    @classmethod
    def get_all_handler_names(cls):
        sql = "SELECT * from handlers;"
        return [row[1] for row in CURSOR.execute(sql).fetchall()]

    @classmethod
    def instance_from_db(cls, row):
        handler = cls(
            id=row[0],
            name=row[1],
            email=row[2],
            phone=row[3],
            hourly_rate=row[4],
        )
        return handler

    @classmethod
    def find_handler_by_id(cls, id):
        sql = """
            SELECT * FROM handlers
            WHERE id = ? 
            LIMIT 1
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        if not row:
            return None
        return cls.instance_from_db(row)

    @classmethod
    def find_handler_by_name(cls, name):
        sql = """
            SELECT * FROM handlers
            WHERE name = ? 
            LIMIT 1
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        if not row:
            return None
        return cls.instance_from_db(row)

    def __init__(self, name, email, phone, hourly_rate, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.hourly_rate = hourly_rate

    def save(self):
        sql = """
            INSERT INTO handlers (name, email, phone, hourly_rate)
            VALUES (?, ?, ?, ?);
        """
        CURSOR.execute(sql, (self.name, self.email, self.phone, self.hourly_rate))
        CONN.commit()
        self.id = CURSOR.lastrowid
