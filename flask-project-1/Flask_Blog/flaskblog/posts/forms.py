from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class CreateNewPost(FlaskForm):
    title = StringField(label='Title', validators=[
        DataRequired(), Length(min=5, max=20)])
    content = TextAreaField(label='Content', validators=[DataRequired()])
    submit = SubmitField(label='Submit Post')
