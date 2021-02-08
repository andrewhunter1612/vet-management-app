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
    return render_template('appointments/index.html')
