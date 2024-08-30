from lib.job import Job


class Handler:

    all = []

    def __init__(self, name, email, hourly_rate):
        self.name = name
        self.email = email
        self.hourly_rate = hourly_rate
        self.__class__.all.append(self)

    def jobs(self):
        return [job for job in Job.all if job.handler == self]

    def get_pets(self):
        return [job.pet for job in self.jobs()]

    def __repr__(self):
        return f"<Handler: {self.name}>"
