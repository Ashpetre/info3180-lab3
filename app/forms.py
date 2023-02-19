from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=255)])
    subject = StringField('Subject', validators=[DataRequired(), Length(max=255)])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')
