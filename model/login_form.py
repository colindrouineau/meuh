from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_wtf import FlaskForm, Form

# Formulaire de connexion
class LoginForm(Form):
    """
        Class Login Form inherits Form
    """

    id = StringField('Identifiant')
    password = PasswordField('Password')
    submit = SubmitField('Submit')
