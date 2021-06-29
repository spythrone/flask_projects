from flask import render_template, url_for, redirect, flash, request, Blueprint
from flaskblog import db
from flaskblog.users.forms import RegistrationForm, LoginForm, UpdateAccountProfile
from flaskblog.users.utils import save_picture
from flaskblog.users.models import User
from flaskblog.posts.models import Posts
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required


users = Blueprint('users', __name__, template_folder='templates')


@users.route('/register', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        password_hash = generate_password_hash(reg_form.password.data)
        user = User(username=reg_form.username.data,
                    email=reg_form.email.data, password=password_hash)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for { reg_form.username.data } !', 'success')
        return redirect(url_for('users.login'))
    else:
        return render_template('users/registration.html', title='Registration', form=reg_form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    log_form = LoginForm()
    if log_form.validate_on_submit():
        user = User.query.filter_by(email=log_form.email.data).first()
        if user and check_password_hash(user.password, log_form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash(f'Login failed please check email and password !', 'danger')
    return render_template('users/login.html', title='Login', form=log_form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/account', methods=['GET', 'POST'])
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
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for(
        'static', filename='profile_pics/' + current_user.image_file)
    return render_template('users/account.html', title='Account',
                           image_file=image_file, form=form)


@users.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get("page", 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Posts.query.filter_by(user=user).order_by(
        Posts.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('users/user_posts.html', posts=posts, user=user)
