from models.owner import Owner
from db.run_sql import run_sql


def save_new_owner(owner):
    sql = "INSERT INTO owners (name, address, phone_number) Values (%s, %s, %s) RETURNING * "
    values = [owner.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    owner.id = id
    return owner

def select_owner(id):
    sql = "SELECT * FROM owners WHERE id=%s"
    value = [id]
    result = run_sql(sql, value)
    if result is not None:
        owner = Owner(result["name"], result["phone_number"], result["address"])
        return owner

def select_all_owners():
    results = run_sql("SELECT * FROM owners")
    owners = []
    for result in results:
        owner = Owner(result["name"], result["phone_number"], result["address"])
        owners.append(owner)
    return owners
