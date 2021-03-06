from flask import Flask, Blueprint, redirect, render_template, request
import repositories.owner_repository as owner_repository
from models.owner import Owner


owner_blueprint = Blueprint("owner", __name__)

@owner_blueprint.route('/owners')
def owner_page():
    owners = owner_repository.select_all_owners()
    owners = sorted(owners, key=lambda owner:owner.name)
    return render_template('/owners/index.html', owners=owners)

@owner_blueprint.route('/owners/new')
def new_owner_page():
    return render_template('owners/new.html')

@owner_blueprint.route('/owners/new', methods=["POST"])
def add_new_owner():
    name = request.form["name"].capitalize()
    phone_number = request.form["phone"]
    address = request.form["address"].capitalize()
    owner = Owner(name, phone_number, address)
    owner_repository.save_new_owner(owner)
    return redirect('/owners')

@owner_blueprint.route('/owners/<id>/edit')
def edit_owner_page(id):
    chosen_owner = owner_repository.select_owner(id)
    owners = owner_repository.select_all_owners()
    owners = sorted(owners, key=lambda owner:owner.name)
    animals = owner_repository.get_all_animals(chosen_owner)
    return render_template('owners/index.html', animals=animals, owners=owners, more_info=True, edit_info=True, chosen_owner=chosen_owner)

@owner_blueprint.route('/owners/<id>/edit', methods=["POST"])
def edit_owner(id):
    name = request.form["name"]
    phone_number = request.form["phone"]
    address = request.form["address"]
    owner = Owner(name, phone_number, address, id)
    owner_repository.update_owner(owner)
    return redirect('/owners/'+id+'/more')

@owner_blueprint.route('/owners/<id>/more')
def more_owner_info(id):
    owners = owner_repository.select_all_owners()
    print(len(owners))
    owners = sorted(owners, key=lambda owner:owner.name)
    chosen_owner = owner_repository.select_owner(id)
    animals = owner_repository.get_all_animals(chosen_owner)
    return render_template('/owners/index.html', animals=animals, more_info=True, chosen_owner=chosen_owner, owners=owners)

@owner_blueprint.route('/owners/<id>/delete')
def delete_owner_page(id):
    owner = owner_repository.select_owner(id)
    owner_repository.archive_owner(owner)
    return redirect('/owners')
