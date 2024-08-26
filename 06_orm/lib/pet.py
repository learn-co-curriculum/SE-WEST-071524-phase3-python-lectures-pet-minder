# Stretch Goal: Include Association with Owner

# Pet Attributes: 
# name: string 
# species: string 
# breed: string 
# temperament:string 

# Stretch Goal
# owner_id:int

import sqlite3

CONN = sqlite3.connect('lib/resources.db')
CURSOR = CONN.cursor()

class Pet:
    
    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes

    def __init__(self, name, species, breed, temperament, owner_id, id=None):
        self.id = id
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament
        self.owner_id = owner_id

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
                owner_id INTEGER)
        """

    CURSOR.execute(sql)

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pets
        """

        CURSOR.execute(sql)

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB

    def save(self):
        sql = """
            INSERT INTO pets (name, species, breed, temperament, owner_id)
            VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.species, self.breed, self.temperament, self.owner_id))

        self.id = CURSOR.lastrowid

    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB

    @classmethod
    def create(cls, name, species, breed, temperament, owner_id):
        pet = cls(name, species, breed, temperament, owner_id)
        pet.save()
        
        return pet

    # ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB

    @classmethod
    def new_from_db(cls, row):
        pet = cls(
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4],
            owner_id=row[5],
            id=row[0]
        )

        return pet

    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM pets
        """

        return [cls.new_from_db(row) for row in CURSOR.execute(sql).fetchall()]

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

        return Pet(
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4],
            owner_id=row[5],
            id=row[0]
        )

    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB

        # If No "pet" Found, return "None"

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM pets
            WHERE id = ?
            LIMIT 1
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        if not row:
            return None

        return Pet(
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4],
            owner_id=row[5],
            id=row[0]
        )

    # ✅ 10. Add "find_or_create_by" Class Method to:

        #  Find and Retrieve "pet" Instance w/ All Attributes

        # If No "pet" Found, Create New "pet" Instance w/ All Attributes

    @classmethod
    def find_or_create_by(cls, name=None, species=None, breed=None, temperament=None, owner_id=None):
        sql = """
            SELECT * FROM pets
            WHERE (name, species, breed, temperament, owner_id) = (?, ?, ?, ?, ?)
            LIMIT 1
        """

        row = CURSOR.execute(sql, (name, species, breed, temperament, owner_id)).fetchone()
        if not row:
            sql = """
                INSERT INTO pets (name, species, breed, temperament, owner_id)
                VALUES (?, ?, ?, ?, ?)
            """

            CURSOR.execute(sql, (name, species, breed, temperament, owner_id))
            return Pet(
                name=name,
                species=species,
                breed=breed,
                temperament=temperament,
                owner_id=owner_id,
                id=CURSOR.lastrowid
            )

        return Pet(
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4],
            owner_id=row[5],
            id=row[0]
        )

    # ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All Attributes

    def update(self):
        sql = """
            UPDATE pets
            SET name = ?,
                breed = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.breed, self.id))
