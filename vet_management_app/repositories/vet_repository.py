from db.run_sql import run_sql
from models.vet import Vet


def save_new_vet(vet):
    sql = "INSERT INTO vets (name) VALUES (%s) RETURNING *"
    values = [vet.name]
    results = run_sql(sql, values)
    vet.id  = results[0]["id"]
    
def select_vet(id):
    sql = "SELECT * FROM vets WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)
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

