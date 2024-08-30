#!/usr/bin/env python3
# Class Attributes and Methods
from lib.job import Job


class Pet:

    total_pets = 0
    all = []

    @classmethod
    def increase_pets(cls, increment=1):
        cls.total_pets += increment

    def __init__(self, name, age, breed, temperament, image_url):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.image_url = image_url
        self._owner = None
        # Pet.total_pets += 1
        # Pet.increase_pets()
        self.__class__.increase_pets()
        self.__class__.all.append(self)
        # self.jobs = [] // not Single Source of Truth, and not applicable for SQL db

    # 6✅. Create a class method increase_pets that will increment total_pets
    # replace Pet.total_pets += 1 in __init__ with increase_pets()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) != "str":
            raise ValueError("must be string")
        self._name = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        from lib.owner import Owner

        if not isinstance(value, Owner):
            raise TypeError("Owner must be an instance of Owner class")
        self._owner = value

    def print_pet_details(self):
        print(
            f"""
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
            image_url:{self.image_url}
        """
        )

    def book_job(self, date, duration, handler):
        Job(self, date, duration, handler)

    def jobs(self):
        return [job for job in Job.all if job.pet == self]

    def __repr__(self):
        return f"<Pet name: {self.name} | breed: {self.breed}>"
