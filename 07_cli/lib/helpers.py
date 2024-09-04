from datetime import datetime

from handler import Handler
from job import Job
from pick import pick


def add_job_to_pet(pet):
    handler_names = Handler.get_all_handler_names()
    title = "Which handler will be taking care of your pet?"
    handler_name, index = pick(handler_names, title)
    handler = Handler.find_handler_by_name(handler_name)
    req_type = "What type of job are you requesting?"
    request_choice, index = pick(["Walk", "Drop-in", "Boarding"], req_type)
    date_string = input("Enter date and timein the format YYYY-MM-DD HH:MM:SS")
    date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    note = input("Enter any special notes for the handler")
    job = Job(
        request=request_choice,
        handler_id=handler.id,
        pet_id=pet.id,
        date=date,
        notes=note,
        fee=handler.hourly_rate,
    )
    job.save()
