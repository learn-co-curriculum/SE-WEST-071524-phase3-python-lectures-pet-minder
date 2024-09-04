import sqlite3

CONN = sqlite3.connect("lib/resources.db")
CURSOR = CONN.cursor()


class Job:

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS jobs;
        """
        CURSOR.execute(sql)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS jobs
                (id INTEGER PRIMARY KEY,
                request TEXT,
                date TEXT,
                notes TEXT,
                fee FLOAT,
                pet_id INTEGER,
                handler_id INTEGER);
        """
        CURSOR.execute(sql)

    @classmethod
    def instance_from_db(cls, row):
        job = cls(
            id=row[0],
            request=row[1],
            date=row[2],
            notes=row[3],
            fee=row[4],
            pet_id=row[5],
            handler_id=row[6],
        )
        return job

    @classmethod
    def get_jobs_by_pet_id(cls, id):
        sql = """
            SELECT jobs.*
            FROM jobs
            WHERE jobs.pet_id =?
        """
        return [
            cls.instance_from_db(row) for row in CURSOR.execute(sql, (id,)).fetchall()
        ]

    def __init__(self, request, date, notes, fee, pet_id, handler_id, id=None):
        self.id = id
        self.request = request
        self.date = date
        self.notes = notes
        self.fee = fee
        self.pet_id = pet_id
        self.handler_id = handler_id

    def save(self):
        sql = """
            INSERT INTO jobs (request, date, notes, fee, pet_id, handler_id)
            VALUES (?, ?, ?, ?, ?, ?);
        """
        CURSOR.execute(
            sql,
            (
                self.request,
                self.date,
                self.notes,
                self.fee,
                self.pet_id,
                self.handler_id,
            ),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
