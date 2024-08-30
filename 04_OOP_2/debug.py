#!/usr/bin/env python3
# 📚 Review With Students:
# Introduction to Object Oriented programming, classes, instances, methods

from lib.cat import *
from lib.handler import *
from lib.job import *

# Importing the pet class
from lib.pet import *

# Instances of the pet classes
rose = Cat("rose", 11, "domestic longhair", "sweet", "rose.jpg", True)
# rose = Pet("rose", 11, "domestic longhair", "sweet", "rose.jpg")
cookie = Pet("cookie", 1, "Dachshund", "hyper", "cookie.jpg")
princess_grace = Cat(
    "princess grace", 7, "domestic longhair", "affectionate", "gracy.png", False
)

jae = Handler("Jae", "jae@mail.com", 30)
kevin = Handler("Kevin", "kevin@mail.com", 32)

rose.book_job("9-6-24", 2, jae)
rose.book_job("9-9-24", 3, kevin)
cookie.book_job("9-10-24", 1, jae)


import ipdb

ipdb.set_trace()
