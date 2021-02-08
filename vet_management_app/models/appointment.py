class Appointment:
    def __init__(self, date, time, vet, animal, additional_notes=None, id=None):
        self.date = date
        self.time = time
        self.vet = vet
        self.animal = animal
        self.additional_notes = additional_notes
        self.id = id