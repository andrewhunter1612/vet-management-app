from flask import Flask, Blueprint, redirect, render_template, request
import repositories.animal_repository as animal_repository


animal_blueprint = Blueprint("animal", __name__)

