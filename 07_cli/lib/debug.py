#!/usr/bin/env python3

from owner import CONN, CURSOR, Owner
from pet import CONN, CURSOR, Pet

# sql = """
#     DROP TABLE IF EXISTS pets,
#     DROP TABLE IF EXISTS owner;
# """

# CURSOR.execute(sql)

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()

Pet.drop_table()
Pet.create_table()
spot = Pet("spot", "dog", "chihuahua", "feisty", 1)

try:
    spot.save()
except Exception as e:
    print(f"An error occurred while saving: {e}")
# finally:
#     CONN.close()
slash = Pet.create("Slash", "dog", "chihuahua", "chill", 3)

all_pets = Pet.get_all()
for pet in all_pets:
    print(pet)

import ipdb

ipdb.set_trace()
