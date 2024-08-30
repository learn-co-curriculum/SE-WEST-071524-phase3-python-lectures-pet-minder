class Job:

    all = []

    def __init__(self, pet, date, duration, handler=None):
        self.pet = pet
        self.handler = handler
        self.date = date
        self.duration = duration
        self.__class__.all.append(self)

    def __repr__(self):
        return f"<Job pet: {self.pet.name} >"
