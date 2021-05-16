import secrets
import os
from PIL import Image
from flask import Flask, render_template, url_for, redirect, flash, request
from flaskblog import app, db, login_manager
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountProfile
from flaskblog.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required

posts = [{
    'author': 'Author1',
    'title': 'Title1',
    'content': 'Content1',
},
    {
    'author': 'Author1',
    'title': 'Title1',
    'content': 'Content1',
}]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)



@app.route('/register', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        password_hash = generate_password_hash(reg_form.password.data)
        user = User(username=reg_form.username.data, email=reg_form.email.data, password=password_hash)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for { reg_form.username.data } !', 'success')
        return redirect(url_for('login'))
    else:
        return render_template('registration.html', title='Registration', form=reg_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    log_form = LoginForm()
    if log_form.validate_on_submit():
        user = User.query.filter_by(email=log_form.email.data).first()
        if user and check_password_hash(user.password, log_form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login failed please check email and password !', 'danger')
    return render_template('login.html', title='Login', form=log_form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/about')
@login_required
def about():
    return "<h1>About Page</h1>"

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountProfile()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)

# @login_manager.unauthorized_handler
# def unauthorized_redirect():
#     flash(f'Use need to login first !', 'info')
#     return redirect(url_for('login'))