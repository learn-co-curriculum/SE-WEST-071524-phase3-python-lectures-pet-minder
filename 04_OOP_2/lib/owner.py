from lib.pet import *


class Owner:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be of the Pet class")
        pet.owner = self

    def __repr__(self):
        return f"<Owner: {self.name}>"
