import flask
from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#variables globales (temporaire)
FIRST_NAME = 'ahhhhh'
LAST_NAME = 'lol'

d={'first_name':FIRST_NAME, 'last_name':LAST_NAME}
#inscription
@app.route('/', methods=['GET', 'POST'])
def signup():
    form=MyForm(request.form)
    if form.submit.data:
        d['first_name']=form.first_name.data
        d['last_name']=form.last_name.data
        return redirect(url_for('home'))
    return render_template('signup.html', form=form)

@app.route('/home')
def home():
    return (d['first_name'] + ' ' + d['last_name'])

class MyForm(Form):
    first_name = StringField('First Name')
    last_name  = StringField('Last Name')
    submit = SubmitField('Submit') 

app.run()