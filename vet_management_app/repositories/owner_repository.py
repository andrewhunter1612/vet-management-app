from models.owner import Owner
from db.run_sql import run_sql
from models.animal import Animal

import repositories.vet_repository as vet_repository


def save_new_owner(owner):
    sql = "INSERT INTO owners (name, address, phone_number, archived) Values (%s, %s, %s, %s) RETURNING * "
    values = [owner.name, owner.address, owner.phone_number, owner.archived]
    results = run_sql(sql, values)
    id = results[0]["id"]
    owner.id = id
    return owner

def select_owner(id):
    sql = "SELECT * FROM owners WHERE id=%s"
    value = [id]
    result = run_sql(sql, value)[0]
    if result is not None:
        owner = Owner(result["name"], result["phone_number"], result["address"], result["id"])
        return owner

def select_all_owners():
    results = run_sql("SELECT * FROM owners WHERE archived=%s", ["FALSE"])
    owners = []
    for result in results:
        owner = Owner(result["name"], result["phone_number"], result["address"], result["id"])
        owners.append(owner)
    return owners

def update_owner(owner):
    sql = "UPDATE owners SET (name, phone_number, address) = (%s, %s, %s) WHERE id = %s"
    values = [owner.name, owner.phone_number, owner.address, owner.id]
    run_sql(sql, values)

def get_all_animals(owner):
    sql = "SELECT * FROM animals WHERE owner_id=%s"
    value = [owner.id]
    results = run_sql(sql, value)
    animals = []
    for result in results:
        vet = vet_repository.select_vet(result["vet_id"])
        animal = Animal(result["name"], result["date_of_birth"], result["animal_type"], owner, result["treatment_notes"], vet, result["id"])
        animals.append(animal)
    return animals

def archive_owner(owner):
    sql = "UPDATE owners SET archived = %s WHERE id=%s"
    owner.update_archived(True)
    values = [owner.archived, owner.id]
    run_sql(sql, values)


