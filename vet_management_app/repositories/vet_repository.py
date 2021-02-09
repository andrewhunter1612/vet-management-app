from db.run_sql import run_sql
from models.vet import Vet


def save_new_vet(vet):
    sql = "INSERT INTO vets (name) VALUES (%s) RETURNING *"
    values = [vet.name]
    results = run_sql(sql, values)
    vet.id  = results[0]["id"]
    
def select_vet(id):
    sql = "SELECT * FROM vets WHERE id=%s"
    value = [id]
    result = run_sql(sql, value)[0]
    if result is not None:
        vet = Vet(result["name"], result["id"])
        return vet

def select_all_vets():
    results = run_sql( "SELECT * FROM vets")
    vets = []
    for result in results:
        vet = Vet(result["name"], result["id"])
        vets.append(vet)
    return vets

def update_vet(vet):
    sql = "UPDATE vets SET name = %s WHERE id =%s"
    values = [vet.name, vet.id]
    run_sql(sql, values)

def archive_vet(vet):
    vet.update_archived(True)
    sql = "UPDATE vets SET archived = %s WHERE id=%s"
    values = [vet.archived, vet.id]
    run_sql(sql, values)