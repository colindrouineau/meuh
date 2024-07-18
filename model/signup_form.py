from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_wtf import FlaskForm, Form

#Formulaire d'inscription
class SignupForm(Form):
    """
        Class Signup Form inherits Form
    """

    id = StringField('Identifiant')
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    password = PasswordField('Password')
    email = StringField('Email')
    submit = SubmitField('Submit')