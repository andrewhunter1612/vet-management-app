class Animal:
    def __init__(self, name, date_of_birth, animal_type, owner, treatment_notes, vet, id=None):   
        self.name = name
        self.date_of_birth = date_of_birth
        self.animal_type = animal_type
        self.owner = owner
        self.treatment_notes = treatment_notes
        self.vet = vet
        self.id = id