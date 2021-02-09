from flask import Flask, Blueprint, redirect, render_template, request
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.appointment_repository as appointment_repository
from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
from models.appointment import Appointment 

appointment_blueprint = Blueprint("appointment", __name__)

@appointment_blueprint.route('/appointments')
def index():
    appointments = appointment_repository.select_all_appointments()
    appointments = sorted(appointments, key=lambda appointment:appointment.date)
    return render_template('appointments/index.html', appointments=appointments)


@appointment_blueprint.route('/appointments/new')
def new_appointment_page():
    vets = vet_repository.select_all_vets()
    animals = animal_repository.select_all_animals()
    return render_template('appointments/new.html', chosen=False, animals=animals, vets=vets)

@appointment_blueprint.route('/appointments/new/<id>')
def new_animal_appointment_page(id):
    animal = animal_repository.select_animal(id)
    vets = vet_repository.select_all_vets()
    animals = animal_repository.select_all_animals()
    return render_template('appointments/new.html', chosen=True, chosen_animal=animal, animal=animal, animals=animals, vets=vets)

@appointment_blueprint.route('/appointments/new', methods=["POST"])
def add_new_appointment():
    date = request.form["date"]
    time = request.form["time"]
    notes = request.form["notes"]
    vet = vet_repository.select_vet(request.form["vet_id"])
    animal = animal_repository.select_animal(request.form["animal_id"])
    appointment = Appointment(date, time, vet, animal, notes)
    appointment_repository.save_new_appointment(appointment)
    return redirect('/appointments')

