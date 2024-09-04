# Stretch Goal: Include Association with Owner

# Pet Attributes:
# name: TEXT
# species: TEXT
# breed: TEXT
# temperament: TEXT

# Stretch Goal
# owner_id: INTEGER

import sqlite3

CONN = sqlite3.connect("lib/resources.db")
CURSOR = CONN.cursor()


class Pet:

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pets
                (id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                breed TEXT,
                temperament TEXT,
                owner_id INTEGER);
        """
        CURSOR.execute(sql)

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pets;
        """
        CURSOR.execute(sql)

    # ✅ 6. Add "instance_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB
    @classmethod
    def instance_from_db(cls, row):
        pet = cls(
            id=row[0],
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4],
            owner_id=row[5],
        )
        return pet

    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB
    @classmethod
    def get_all_pets(cls):
        sql = "SELECT * FROM pets;"
        return [cls.instance_from_db(row) for row in CURSOR.execute(sql).fetchall()]

    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB
    @classmethod
    def create(cls, name, species, breed, temperament, owner_id):
        pet = cls(name, species, breed, temperament, owner_id)
        pet.save()
        return pet

    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB

    # If No "pet" Found, return "None"
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM pets
            WHERE name = ? 
            LIMIT 1
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        if not row:
            return None
        return cls.instance_from_db(row)

    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB

    # If No "pet" Found, return "None"

    @classmethod
    def find_pet_by_id(cls, id):
        sql = """
            SELECT * FROM pets
            WHERE id = ? 
            LIMIT 1
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        if not row:
            return None
        return cls.instance_from_db(row)

    # ✅ 10. Add "find_or_create_by" Class Method to:
    @classmethod
    def find_or_create_by(
        cls, name=None, species=None, breed=None, temperament=None, owner_id=None
    ):
        sql = """
            SELECT * FROM pets
            WHERE (name, species, breed, temperament, owner_id) = (?, ?, ?, ?, ?)
            LIMIT 1
        """
        row = CURSOR.execute(
            sql, (name, species, breed, temperament, owner_id)
        ).fetchone()
        if not row:
            return cls.create(name, species, breed, temperament, owner_id)
        return cls.instance_from_db(row)

    #  Find and Retrieve "pet" Instance w/ All Attributes

    # If No "pet" Found, Create New "pet" Instance w/ All Attributes

    # ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All Attributes

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    def __init__(self, name, species, breed, temperament, owner_id, id=None):
        self.id = id  # primary
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament
        self.owner_id = owner_id  # foreign key

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB
    def save(self):
        sql = """
            INSERT INTO pets (name, species, breed, temperament, owner_id)
            VALUES (?, ?, ?, ?, ?);
        """
        CURSOR.execute(
            sql, (self.name, self.species, self.breed, self.temperament, self.owner_id)
        )
        CONN.commit()
        self.id = (
            CURSOR.lastrowid
        )  # assigns the pk id created by db to the local instance of pet

    def __repr__(self):
        return f"<Pet {self.id}: {self.name} | {self.species}>"
