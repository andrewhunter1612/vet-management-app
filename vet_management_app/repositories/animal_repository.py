from db.run_sql import run_sql
from models.animal import Animal

def save_new_animal(animal):
    sql = "INSERT INTO animals(name, animal_type, owner_id, vet_id, treatment_notes) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.date_of_birth, animal.animal_type, animal.owner.id, animal.vet.id, animal.treatment_notes]
    results = run_sql(sql, values)
    if results is not None:
        # TODO add in vet
        # TODO add in owner
        animal = Animal(results["name"], results["date_of_birth"], results[["animal_type"], owner, vet, results["treatment_notes"])
        return animal




