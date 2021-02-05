from flask import Flask, Blueprint, redirect, render_template, request
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
from models.animal import Animal
from models.owner import Owner
from models.vet import Vet


animal_blueprint = Blueprint("animal", __name__)

@animal_blueprint.route('/animals')
def animals_page():
    animals = animal_repository.select_all_animals()
    return render_template('/animals/index.html', title="Animals", animals=animals)

@animal_blueprint.route('/animals/new')
def new_animal_page():
    owners = owner_repository.select_all_owners()
    vets = vet_repository.select_all_vets()
    return render_template('/animals/new.html', vets=vets, owners=owners)

@animal_blueprint.route('/animals', methods=["POST"])
def add_new_animal():
    name = request.form["name"]
    dob = request.form["dob"]
    animal_type = request.form["animal_type"]
    treatment_notes = request.form["treatment_notes"]
    print(request.form["owner_id"])
    print(request.form["vet_id"])
    owner = owner_repository.select_owner(request.form["owner_id"])
    vet = vet_repository.select_vet(request.form["vet_id"])

    new_animal = Animal(name, dob, animal_type, owner, treatment_notes, vet)
    animal_repository.save_new_animal(new_animal)
    return redirect('/animals')