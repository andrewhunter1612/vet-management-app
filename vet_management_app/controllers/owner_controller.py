from flask import Flask, Blueprint, redirect, render_template, request
import repositories.owner_repository as owner_repository


owner_blueprint = Blueprint("owner", __name__)



