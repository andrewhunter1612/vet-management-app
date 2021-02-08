from flask import Flask, render_template
from controllers.animal_controller import animal_blueprint
from controllers.vet_controller import vet_blueprint
from controllers.owner_controller import owner_blueprint
from controllers.appointment_controller import appointment_blueprint

app = Flask(__name__)

app.register_blueprint(animal_blueprint)
app.register_blueprint(vet_blueprint)
app.register_blueprint(owner_blueprint)
app.register_blueprint(appointment_blueprint)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)