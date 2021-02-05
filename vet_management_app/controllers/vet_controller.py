from flask import Flask, Blueprint, redirect, render_template, request
import repositories.vet_repository as vet_repository


vet_blueprint = Blueprint("vet", __name__)

@vet_blueprint.route('/vets')
def vets_page():
    return render_template('/vets/index.html')
