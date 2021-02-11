from db.run_sql import run_sql
from models.appointment import Appointment 
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository
import pdb


def save_new_appointment(appointment):
    sql = "INSERT INTO appointments (date, time, vet_id, animal_id, additional_notes) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [appointment.date, appointment.time, appointment.vet.id, appointment.animal.id, appointment.additional_notes]
    result = run_sql(sql, values)
    appointment.id = result[0]["id"]
    return appointment


def select_all_appointments():
    sql = "SELECT * FROM appointments"
    results = run_sql(sql)
    appointments =[]
    for result in results:
        animal = animal_repository.select_animal(result["animal_id"])
        vet = vet_repository.select_vet(result["vet_id"])
        appointment = Appointment(result["date"], result["time"], vet, animal, result["additional_notes"], result["id"])
        appointments.append(appointment)
    return appointments


def select_appointment(id):
    sql = "SELECT * FROM appointments WHERE id=%s"
    value = [id]
    result = run_sql(sql, value)[0]
    if result is not None:
        vet = vet_repository.select_vet(result["vet_id"])
        animal = animal_repository.select_animal(result["animal_id"])
        appointment = Appointment(result["date"], result["time"], vet, animal, result["additional_notes"], result["id"])
        return appointment

def delete_appointment(id):
    sql = "DELETE FROM appointments WHERE id=%s"
    value = [id]
    run_sql(sql, value)

def update_appointment(appointment):
    sql = "UPDATE appointments SET (date, time, vet_id, animal_id, additional_notes) = (%s, %s, %s, %s, %s) WHERE id=%s"
    values = [appointment.date, appointment.time, appointment.vet.id, appointment.animal.id, appointment.additional_notes, appointment.id]
    result = run_sql(sql, values)

def filter_appointments(date, vet_id, animal_id):
    filter_values_to_match = f"{bool(date)} {bool(vet_id)} {bool(animal_id)}"
  
    filter_dictionary = {
        "False False False": "",
        "True False False": f"WHERE date = '{date}'",
        "False False True": f"WHERE animal_id = {animal_id}",
        "False True False": f"WHERE vet_id = {vet_id}",
        "True False True": f"WHERE date = '{date}' AND animal_id =  {animal_id}",
        "True True False": f"WHERE date = '{date}' AND vet_id = {vet_id}",
        "False True True": f"WHERE vet_id = {vet_id} AND animal_id = {animal_id}",
        "True True True": f"WHERE date = '{date}' AND vet_id = {vet_id} AND animal_id = {animal_id}"
    }

    sql = f"SELECT * FROM appointments {filter_dictionary[filter_values_to_match]}"
    
    results = run_sql(sql)
    appointments = []
    for result in results:
        
        # if (vet_id != "" and int(vet_id) != result["vet_id"]) or (animal_id != "" and int(animal_id) != result["animal_id"]) or (date != "" and date != result["date"]):
        #     continue
        vet = vet_repository.select_vet(result["vet_id"])
        animal = animal_repository.select_animal(result["animal_id"])
        appointment = Appointment(result["date"], result["time"], vet, animal, result["additional_notes"], result["id"])
        appointments.append(appointment)
    return appointments


