from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = '90340db44f34e72860227892db30cc5a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


from flaskapp.myapp.routes import myapp_blueprint
app.register_blueprint(myapp_blueprint, url_prefix="/users")


@app.route('/')
def home():
    return redirect(url_for('myapp.show_users'))