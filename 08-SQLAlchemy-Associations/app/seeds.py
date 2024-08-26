
from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Pet, Owner, Job, Handler

if __name__ == '__main__':
    engine = create_engine('sqlite:///pet_app.db')
    Session = sessionmaker(bind=engine)
    session = Session()
#2.a ✅ Add delete methods for Pet and Owner to clear the database before each seeding
    session.query(Job).delete()
    session.query(Handler).delete()
    session.query(Pet).delete()
    session.query(Owner).delete()
    #Initialize faker
    fake = Faker()

    #Create an array for species with "CAT" and "Dog"
    species = ["CAT", "DOG"]

    #Create an array of cat breeds
    cat_breeds = ["Domestic long hair", "Domestic short hair", "Siamese", "Ragdoll", "Sphynx", "Burmese"]
    #Create an array of dog breeds
    dog_breeds = ["Mix", "Husky", "Malamute", "Dachshound", "Samoyed", "Shiba Inu", "Corgi"]
    #Create an array of temperaments 
    temperament = ["Calm", "Nervous", "Mischievous", "Aggressive", "Hyper" ]
    
    #Create an empty array for owners
    owners = []
    #Create a for loop that iterates 50 times
    for _ in range(50):
        #Create an owner using data from faker
        owner = Owner(
            name=f"{fake.first_name()} {fake.last_name()}",
            email=fake.email(),
            phone= random.randint(1000000000, 9999999999) ,
            address=fake.address()
        )

        #Use .add and .commit to save the owner one at a time, so we maintain the owner ID in our instance.
        session.add(owner)
        session.commit()
        #Append the owner to the owners array
        owners.append(owner)
    
    #Create an empty pets array
    pets = []
    #Create a for loop that iterates over the owners array
    for owner in owners:
        #Create a for loop that iterates 1 - 3 times
        for _ in range(random.randint(1,3)):
            #Use faker and the species, cat breeds, dog breeds and temperament array to create a pet
            rand_species = random.choice(species)
            pet = Pet(
                name=fake.name(),
                species= rand_species,
                breed= random.choice(cat_breeds) if rand_species == "CAT" else random.choice(dog_breeds),
                temperament= random.choice(temperament),
                owner_id = owner.id
            )
            #Use .add and .commit to save the pet to the database
            session.add(pet)
            session.commit()
            #Append the pet to the pets array
            pets.append(pet)
#3✅ run the seed file and head over to debug.py to test out your one to many
#----------------------------------------------------- 

#5.✅ Create a empty array set to handlers
    handlers = []
    #Create a for loop that iterates 50 times
    for _ in range(50):
        #Create a handler with faker data 
        handler = Handler(
            name=f"{fake.first_name()} {fake.last_name()}",
            email=fake.email(),
            phone= random.randint(1000000000, 9999999999) ,
            hourly_rate=random.uniform(25.50, 80.50)
        )
        #Use .add and .commit to save the handler to the database
        session.add(handler)
        session.commit()
        #Append handler to handlers
        handlers.append(handler)
    
    #Create an array of requests, "Walk", "Drop-in" and "Boarding"
    requests = ["Walk", "Drop-in", "Boarding"]
    #Create an empty array and set it to jobs
    jobs = []
    #Create a for loop that iterates over the handlers array
    for handler in handlers:
        #Create a for loop that iterates 1 - 10 times
        for _ in range(random.randint(1,10)):
            #Create a Job using faker, the request array and pets array
            job = Job(
                request=random.choice(requests),
                date= fake.date_this_year(),
                notes= fake.sentence(),
                fee= handler.hourly_rate,
                handler_id = handler.id,
                pet_id = random.choice(pets).id
            )
            #append the job to the jobs array
            jobs.append(job)    
        #Bulk save the jobs (we wont need their id)
    session.bulk_save_objects(jobs)
    session.commit()
    session.close()

#6.✅ Run the seeds file and head over to debug.py to test out your Many to Many 