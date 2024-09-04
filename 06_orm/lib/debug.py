#!/usr/bin/env python3

from owner import Owner
from pet import Pet

# sql = """
#     DROP TABLE IF EXISTS pets;
# """

# CURSOR.execute(sql)

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()
Pet.drop_table()
Pet.create_table()

try:
    spot = Pet("spot", "dog", "chihuahua", "feisty", 1)
    # spot = Pet("spot", "dog", "chihuahua")
    spot.save()
except Exception as e:
    print(f"An error occured while saving: {e}")
# finally:
#     CONN.close()

brigid = Pet.create("Brigid", "cat", "tabby", "fiesty", 2)


import ipdb

ipdb.set_trace()
