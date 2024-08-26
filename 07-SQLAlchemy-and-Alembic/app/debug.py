
# 3.✅ CRUD practice
# To run the file run `python3 console.py` in the app directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Pet)

if __name__ == '__main__':
    #3.1 ✅ Create the engine
    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)
    #3.2 ✅ Create sessions and bind o the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    #3.3 ✅  -- Creating records
        # Create a pet and save it to the data base with session.add and session.commit
    rose = Pet(name="Rose", species="Cat", breed="Domestic longhair", temperament="chill", owner_id=1)
        # Create multiple pets and bulk save them with  session.bulk_save_objects and session.commit
    luke = Pet(name="Luke", species="Cat", breed="Domestic longhair", temperament="mischievous", owner_id=2)

        #session.add(rose)
        #Note: bulk save will not contain the id
    session.bulk_save_objects([rose, luke])
    session.commit()
    print(rose)
        #verify by checking the db 
    #3.4 ✅ Read
        # Get all with session.query
        # Print the pets 
    pets = session.query(Pet)
    print([pet for pet in pets])
        #Get all of the pet names and print them with session.query
    names = [name for name in session.query(Pet.name)]
    print(names)
        #Get all the pet names and print them in order with session.query and order_by
    names_in_order = [name for name in session.query(Pet.name).order_by(Pet.name)]
    print(names)
        #Get the first pet with session.query and first
    first = session.query(Pet).first()
    print(first)

        #Filter pet by temperament with session.query and filter 
    query = session.query(Pet).filter(Pet.temperament.like('%mischievous%'))
    for record in query:
        print(record)

    #3.5 ✅ Update 
        # Update the pets name and print the updated pet info
    first.name = "Bob"
    session.commit()
    print(first)
        # Update all the pets temperament to 'cool' and print the pets 
    session.query(Pet).update({Pet.temperament: 'Cool'})
    pets = session.query(Pet)
    print([pet for pet in pets])

    #3.6 ✅  Delete
        # Delete one item by querying the first pet, deleting it and committing it
    delete_this_pet = session.query(Pet).first()
    session.delete(delete_this_pet)
    session.commit()
        #delete all the pets with session.query and .delete
    session.query(Pet).delete()
    session.commit()

    # Optional Break point for debugging and testing
    import ipdb; ipdb.set_trace()