import flask
from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_sqlalchemy import SQLAlchemy
from accueil import accueil

#initialisation des databases
db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

#variables globales (temporaire)
FIRST_NAME = ''
LAST_NAME = ''

d={'first_name':FIRST_NAME, 'last_name':LAST_NAME}

#page d'accueil
@app.route('/')
def home():
    return render_template('home.html')

#inscription
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form=MyForm(request.form)
    if form.submit.data:
        d['first_name']=form.first_name.data
        d['last_name']=form.last_name.data
        d['id']=form.id.data
        d['password']=form.password.data
        d['email']=form.email.data
        with app.app_context():
            users=User.query.all()
            if d['id'] in [user.username for user in users]:
                return '<p>Utilisateur déjà existant</p> <hr> <a href="/login">Connectez-vous !</a>'
            if d['email'] in [user.email for user in users]:
                return '<p>Email déjà utilisé</p> <hr> <a href="/login">Connectez-vous !</a>'
            db.create_all()
            db.session.commit()
            create_user(d['id'],d['first_name'], d['last_name'], d['password'], d['email'])
        return redirect(url_for('suite'))
    return render_template('signup.html', form=form)

@app.route('/suite')
def suite():
    return redirect(url_for('accueil'))
    return ('Bienvenue' + d['first_name'] + ' ' + d['last_name']+'!')

class MyForm(Form):
    id=StringField('Identifiant')
    first_name = StringField('First Name')
    last_name  = StringField('Last Name') 
    password = PasswordField('Password')
    email = StringField('Email')
    submit = SubmitField('Submit')

class User(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    first_name=db.Column(db.String(20), nullable=False)
    last_name=db.Column(db.String(20), nullable=False)
    password=db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

def create_user(id,first_name, last_name, password, email):
    user = User(username=id, first_name=first_name, last_name=last_name, password=password, email=email)
    db.session.add(user)
    db.session.commit()

#connexion
class Loginform(Form):
    id=StringField('Identifiant')
    password = PasswordField('Password')
    submit = SubmitField('Submit') 

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=Loginform(request.form)
    if form.submit.data:
        d['id']=form.id.data
        d['password']=form.password.data
        with app.app_context():
            users=User.query.all()
            if d['id'] in [user.username for user in users]:
                user=User.query.filter_by(username=d['id']).first()
                if user.password==d['password']:
                    return redirect(url_for('logged_in'))
            else:
                return '<p>Utilisateur non trouvé</p> <hr> <a href="/signup">Inscrivez-vous !</a>'
    return render_template('login.html', form=form)

@app.route('/logged_in')
def logged_in():
    return redirect(url_for('accueil'))
    return 'Vous êtes connecté'

app.run()