#6✅. Create a subclass of Pet called Cat
    # import Pet from lib.pet
    # Update the instance in debug.py to rose = Cat('rose', 11, 'domestic longhair', 'sweet', 'rose.jpg', True)
from lib.pet import Pet
class Cat(Pet):
#8✅. Create __init__ that takes all the parameters from Pet and a parameter called indoor 
    # Use super to pass the Pet parameters to the super class
    # Add an indoor attribute
    def __init__(self,name, age, breed, temperament, image_url, indoor):
        super().__init__(name, age, breed, temperament, image_url)
        self.indoor = indoor

#7✅. Create a method unique to the Cat subclass called talk which returns the string "Meowwwwwww"
    def talk(self):
        return "Meowwwwwww"

#9✅. Stretch: Create a method called print_pet_details, to match the print_pet_details in Pet    
    def print_pet_details(self):
        #Add super().print_pet_details() and print the indoor attribute
        super().print_pet_details()
        print(f'''
            Indoor:{self.indoor}
            ''')
