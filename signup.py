import flask
from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_sqlalchemy import SQLAlchemy

#initialisation des databases
db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET KEY']='secret'
db.init_app(app)

#variables globales (temporaire)
FIRST_NAME = 'ahhhhh'
LAST_NAME = 'lol'

d={'first_name':FIRST_NAME, 'last_name':LAST_NAME}
#inscription
@app.route('/')
def index():
    return render_template('index_resan.html')

@app.route('/home')
def home():
    return (str(d['first_name']))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form=MyForm(request.form)
    if form.submit.data:
        d['first_name']=form.first_name.data
        d['last_name']=form.last_name.data
        return redirect(url_for('home'))
    return render_template('signup.html', form=form)

class MyForm(Form):
    first_name = StringField('First Name')
    last_name  = StringField('Last Name')
    submit = SubmitField('Submit') ###pb de submit 


#un user
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


#créer un user
def create_user(username, email, password):
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

app.run()