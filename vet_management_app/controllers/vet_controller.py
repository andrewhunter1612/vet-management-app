from flask import Flask, Blueprint, redirect, render_template, request
import repositories.vet_repository as vet_repository
from models.vet import Vet


vet_blueprint = Blueprint("vet", __name__)

@vet_blueprint.route('/vets')
def vets_page():
    vets = vet_repository.select_all_vets()
    vets = sorted(vets, key=lambda vet:vet.name)
    return render_template('/vets/index.html',nav_button_highlighted=True, more_info=False, vets=vets)

@vet_blueprint.route('/vets/new')
def add_new_vet_page():
    return render_template('/vets/new.html')

@vet_blueprint.route('/vets/new', methods=["POST"])
def add_new_vet():
    name = request.form["name"].capitalize()
    vet = Vet(name)
    vet_repository.save_new_vet(vet)
    return redirect('/vets')

@vet_blueprint.route('/vets/<id>/edit')
def edit_vet_page(id):
    vets = vet_repository.select_all_vets()
    vets = sorted(vets, key=lambda vet:vet.name)
    chosen_vet = vet_repository.select_vet(id)
    return render_template('vets/index.html',nav_button_highlighted=True, vets=vets, chosen_vet=chosen_vet, more_info=True, edit_info=True)

@vet_blueprint.route('/vets/<id>/edit', methods=["POST"])
def edit_vet(id):
    name = request.form["name"]
    vet = Vet(name, id)
    vet_repository.update_vet(vet)
    return redirect ('/vets/' + id + '/more')

@vet_blueprint.route('/vets/<id>/more')
def more_info(id):
    vets = vet_repository.select_all_vets()
    vets = sorted(vets, key=lambda vet:vet.name)
    chosen_vet = vet_repository.select_vet(id)
    return render_template('/vets/index.html',nav_button_highlighted=True,  more_info=True, chosen_vet=chosen_vet, vets=vets)

@vet_blueprint.route('/vets/<id>/delete')
def delete_vet(id):
    vet = vet_repository.select_vet(id)
    vet_repository.archive_vet(vet)
    return redirect('/vets')