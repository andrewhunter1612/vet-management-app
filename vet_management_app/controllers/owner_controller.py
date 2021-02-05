from flask import Flask, Blueprint, redirect, render_template, request
import repositories.owner_repository as owner_repository
from models.owner import Owner


owner_blueprint = Blueprint("owner", __name__)

@owner_blueprint.route('/owners')
def owner_page():
    owners = owner_repository.select_all_owners()
    return render_template('/owners/index.html', owners=owners)

@owner_blueprint.route('/owners/new')
def new_owner_page():
    return render_template('owners/new.html')

@owner_blueprint.route('/owners', methods=["POST"])
def add_new_owner():
    name = request.form["name"]
    phone_number = request.form["phone"]
    address = request.form["address"]
    owner = Owner(name, phone_number, address)
    owner_repository.save_new_owner(owner)
    return redirect('')

