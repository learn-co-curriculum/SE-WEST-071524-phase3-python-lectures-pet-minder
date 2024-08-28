#!/usr/bin/env python3

from lib.pet import *

# brigid = Pet()
# simon = Pet()

# brigid.name = "Brigid"

cookie = Pet("Cookie", 5, "Dachshund", "fiesty", "./assets/cookie.jpg")
rose = Pet("Rose", 10, "domestic_longhair", "sweet", "./assets/rose.jpg")

print(cookie)
cookie.print_pet()

rose.age = "ain't nothin' but a number"
print(rose.age)
rose.age = 11
rose.age = 8
print(rose.age)


import ipdb

ipdb.set_trace()
