from flask import redirect, render_template, Blueprint
from flaskapp import app
from .models import Myuser

myapp_blueprint = Blueprint('myapp', __name__, template_folder="templates")


@myapp_blueprint.route('/')
def show_users():
    users = Myuser.query.all()
    return render_template('users.html', users=users)


@myapp_blueprint.route('/create', methods=["POST"])
def create_users():
    pass

@myapp_blueprint.route('/<int:id>')
def show_user_with_id(id):
    return str(id)

