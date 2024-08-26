#!/usr/bin/env python3
# Demonstrate classes 

class Pet:
   # 4. ✅ Define a class attribute total pets and set it to 0
        # Demonstrate the class attribute using debug.py
        # Pet.total_pets -> 0
        # rose.total_pets -> 0
        # cookie.total_pets -> 0
        # Demonstrate updating a class attribute 
        # Pet.total_pets += 1
        # rose.total_pets -> 1
        # cookie.total_pets -> 1
    total_pets = 0
    def __init__(self,name, age, breed, temperament, image_url):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.image_url = image_url
        # 5✅. Update the class attribute whenever an instance is initialized
        # Pet.total_pets += 1
        # Demonstrate total_pets updating with each instance 
        # Pet.total_pets -> 3
        # Pet('luke', 3, 'domestic longhair', 'sleepy', 'luke.jpg')
        # Pet.total_pets -> 4
        self.increase_pets()
    
    # 6✅. Create a class method, increase_pets that will increment total_pets
        # replace Pet.total_pets += 1 in __init__ with increase_pets()
    @classmethod
    def increase_pets(cls, increment=1):
        cls.total_pets += increment

    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
            image_url:{self.image_url}
        ''')




