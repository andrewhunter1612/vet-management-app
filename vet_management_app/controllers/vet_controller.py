from flask import Flask, Blueprint, redirect, render_template, request
import repositories.vet_repository as vet_repository
from models.vet import Vet


vet_blueprint = Blueprint("vet", __name__)

@vet_blueprint.route('/vets')
def vets_page():
    vets = vet_repository.select_all_vets()
    return render_template('/vets/index.html', vets=vets)

@vet_blueprint.route('/vets/new')
def add_new_vet_page():
    return render_template('/vets/new.html')

@vet_blueprint.route('/vets', methods=["POST"])
def add_new_vet():
    name = request.form["name"]
    vet = Vet(name)
    vet_repository.save_new_vet(vet)
    return redirect('/vets')