from handler import Handler
from helpers import *
from job import Job
from pet import Pet
from rich import print

# Tasks:
# 1. Show all the pets
# 2. See a pet's details
# 3. See a pet's jobs
# 4. Add a job
# 5. Add a pet (stretch)


# *************
# Interface operations
def display_welcome():
    print("[magenta]Hello! Welcome to [/magenta][bold cyan]Pet Minder![/bold cyan]")


def display_main_menu():
    print("Main Menu")
    print("1. Show all pets")
    print("2. Add a pet")
    print("3. Exit")


def get_main_choice():
    return input("What is your command?")


def display_all_pets():
    pets = Pet.get_all_pets()
    for pet in pets:
        print(f"{pet.id} | {pet.name} | {pet.species}")
    print("What would you like to see?")
    print("1. See more about a pet")
    print("2. Return to main menu")
    choice = input()
    if choice == "1":
        choose_pet_by_id()
    else:
        display_main_menu()


def choose_pet_by_id():
    search_id = input("Enter the id of the pet you want to see")
    pet = Pet.find_pet_by_id(search_id)
    print(
        f"Id: {pet.id}, Name: {pet.name}, Species: {pet.species}, Breed: {pet.breed}, Temperament: {pet.temperament}"
    )
    display_pet_submenu(pet)


def display_pet_submenu(pet):
    print("1. See a pet's jobs")
    print("2. Add a job to a pet")
    print("3. Exit")
    print("What would you like to do?")
    choice = input()
    handle_pet_choice(choice, pet)


def handle_pet_choice(choice, pet):

    if choice == "1":
        show_pet_jobs(pet)
    elif choice == "2":
        add_job_to_pet(pet)
    else:
        display_all_pets()


def show_pet_jobs(pet):
    jobs = Job.get_jobs_by_pet_id(pet.id)
    for job in jobs:
        print(
            f"{job.id} | {job.request} | {job.date} | {job.notes} | ${job.fee:.2f} || with {Handler.find_handler_by_id(job.handler_id).name}"
        )


def add_pet(pet):
    pass


def goodbye():
    print("Thanks for using Pet Minder!")


# *************
# Command line interface
if __name__ == "__main__":
    display_welcome()
    while True:
        display_main_menu()
        choice = get_main_choice()
        print(choice)
        if choice == "1":
            display_all_pets()
        elif choice == "2":
            add_pet()
        else:
            break
    goodbye()
