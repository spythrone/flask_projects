from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.users.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField(label='Username', validators=[
                           DataRequired(), Length(min=5, max=20)])
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[
                             DataRequired(), Length(min=8, max=20)])
    confirm_password = PasswordField(label='Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Submit')

    def validate_username(self, username):
        uname = User.query.filter_by(username=username.data).first()
        if uname:
            raise ValidationError(
                "This username has been taken. Please choose different username")

    def validate_email(self, email):
        uemail = User.query.filter_by(email=email.data).first()
        if uemail:
            raise ValidationError(
                "This email has been taken. Please choose different email")


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[
                             DataRequired(), Length(min=8, max=20)])
    submit = SubmitField(label='Login')


class UpdateAccountProfile(FlaskForm):
    username = StringField(label='Username', validators=[
                           DataRequired(), Length(min=5, max=20)])
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField(label='Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            uname = User.query.filter_by(username=username.data).first()
            if uname:
                raise ValidationError(
                    "This username has been taken. Please choose different username")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    "This email has been taken. Please choose different email")
