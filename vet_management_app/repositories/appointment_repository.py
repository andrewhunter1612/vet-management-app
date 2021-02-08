from db.run_sql import run_sql
from models.appointment import Appointment 
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository


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
    result = run_sql(run_sql, value)[0]
    if result is not None:
        vet = vet_repository.select_vet(result["vet_id"])
        animal = animal_repository.select_animal(result["animal_id"])
        appointment = Appointment(result["date"], result["time"], vet, animal, result["additional_notes"], result["id"])

def delete_appointment(id):
    sql = "DELETE FROM appointments WHERE id=%s"
    value = [id]
    run_sql(sql, value)

def update_appointment(appointment):
    sql = "UPDATE appointments SET (date, time, vet_id, animal_id, additional_notes) = (%s, %s, %s, %s, %s) WHERE id=%s"
    values = [appointment.date, appointment.time, appointment.vet.id, appointment.animal.id, appointment.additional_notes, appointment.id]
    result = run_sql(sql, values)
