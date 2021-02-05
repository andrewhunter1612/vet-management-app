from db.run_sql import run_sql
from models.animal import Animal
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

def save_new_animal(animal):
    sql = "INSERT INTO animals(name, date_of_birth, animal_type, owner_id, vet_id, treatment_notes) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.date_of_birth, animal.animal_type, animal.owner.id, animal.vet.id, animal.treatment_notes]
    results = run_sql(sql, values)
    animal.id = results[0]["id"]
    return animal

def select_animal(id):
    sql = "SELECT * FROM animals WHERE id=%s"
    value = [id]
    result = run_sql(sql, value)[0]
    if result is not None:
        owner = owner_repository.select_owner(result["id"])
        vet = vet_repository.select_vet(result["id"])
        animal = Animal(result["name"], result["date_of_birth"], result["animal_type"], owner, vet, result["treatment_notes"], result["id"])
        return animal

def select_all_animals():
    results = run_sql("SELECT * FROM animals")
    animals = []
    for result in results:
        owner = owner_repository.select_owner(result["id"])
        vet = vet_repository.select_vet(result["id"])
        animal = Animal(result["name"], result["date_of_birth"], result["animal_type"], owner, vet, result["treatment_notes"], result["id"])
        animals.append(animal)
    return animals

def update_animal(animal):
    sql = "UPDATE animals SET (name, date_of_birth, animal_type, owner_id, vet_id, treatment_notes) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.date_of_birth, animal.animal_type, animal.owner.id, animal.vet.id, animal.treatment_notes, animal.id]
    run_sql(sql, values)

    

