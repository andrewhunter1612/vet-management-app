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
    animals = sorted(animals, key=lambda animal:animal.name)
    return render_template('/animals/index.html', animals=animals)

@animal_blueprint.route('/animals/new')
def new_animal_page():
    owners = owner_repository.select_all_owners()
    vets = vet_repository.select_all_vets()
    return render_template('/animals/new.html', vets=vets, owners=owners)

@animal_blueprint.route('/animals/new', methods=["POST"])
def add_new_animal():
    name = request.form["name"].capitalize()
    dob = request.form["dob"]
    animal_type = request.form["animal_type"].capitalize()
    treatment_notes = request.form["notes"].capitalize()
    owner = owner_repository.select_owner(request.form["owner_id"])
    vet = vet_repository.select_vet(request.form["vet_id"])
    new_animal = Animal(name, dob, animal_type, owner, treatment_notes, vet)
    animal_repository.save_new_animal(new_animal)
    return redirect('/animals')

@animal_blueprint.route('/animals/<id>/edit')
def edit_animal_page(id):
    vets = vet_repository.select_all_vets()
    owners = owner_repository.select_all_owners()
    chosen_animal = animal_repository.select_animal(id)
    animals = animal_repository.select_all_animals()
    animals = sorted(animals, key=lambda animal:animal.name)

    dob = chosen_animal.date_of_birth.split('/')
    print(dob)
    print(len(dob))
    if len(dob)==3:
        if len(dob[1]) <2:
            dob[1] = "0" + dob[1]
        dob = dob[2]+"-"+dob[1]+"-"+dob[0]
    print(dob)

    return render_template('animals/index.html', dob=dob, owners=owners, vets=vets, chosen_animal=chosen_animal, animals=animals, edit_info=True, more_info=True)

@animal_blueprint.route('/animals/<id>/edit', methods=["POST"])
def edit_animal(id):
    name = request.form["name"]
    dob = request.form["dob"]
    animal_type = request.form["animal_type"]
    treatment_notes = request.form["notes"]
    owner = owner_repository.select_owner(request.form["owner_id"])
    vet = vet_repository.select_vet(request.form["vet_id"])
    new_animal = Animal(name, dob, animal_type, owner, treatment_notes, vet, id)
    animal_repository.update_animal(new_animal)
    return redirect('/animals/'+id+'/more')

@animal_blueprint.route('/animals/<id>/more')
def more_animal_info(id):
    animals = animal_repository.select_all_animals()
    animals = sorted(animals, key=lambda animal:animal.name)
    chosen_animal = animal_repository.select_animal(id)
    return render_template('animals/index.html', chosen_animal=chosen_animal, more_info=True, animals=animals)

@animal_blueprint.route('/animals/<id>/delete')
def archive_animal(id):
    animal = animal_repository.select_animal(id)
    animal_repository.archive_animal(animal)
    return redirect('/animals')