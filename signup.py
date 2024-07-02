import flask
from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template
from datetime import datetime 

import pathlib as pl 

root_dir = pl.Path(__file__).parent
db_path = root_dir / 'instance' / 'site.db'

#initialisation des databases
db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db.init_app(app)

static_folder = 'static'

#variables globales (temporaire)
FIRST_NAME = ''
LAST_NAME = ''

d={'first_name':FIRST_NAME, 'last_name':LAST_NAME, 'id':''}

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
            if users != []:
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
        d['first_name']=User.query.filter_by(username=d['id']).first().first_name
        d['last_name']=User.query.filter_by(username=d['id']).first().last_name
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

'''
#accueil
@app.route("/accueil")
def accueil():
    current_date = datetime.now().strftime("%d-%m-%Y")
    tasks = ["task_1", "task_2", "task_3"]
    name=[d['first_name'], d['last_name']]
    print(name)
    # il faudrait trouver un moyen d'ajouter les tasks de la journée en fonction de la journée
    # et updater les tasks tous les jours, en les reliant à la base de données ?
    return render_template('index_accueil.html', current_date=current_date, tasks = tasks, name=name)
'''
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)

def create_task(name, date, done=False):
    task = Task(name=name, date=date, done=done)
    db.session.add(task)
    db.session.commit()

with app.app_context():
    db.create_all()
    db.session.commit()
    create_task("task_test1", datetime.now().date())
    create_task("task_test2", datetime.now())

@app.route("/accueil", methods=["GET", "POST"])
def accueil():
    current_date = datetime.now().strftime("%d-%m-%Y")
    tasks= Task.query.filter_by(date=current_date).all()
    completed_tasks = []
    if request.method == "POST":
        completed_tasks = request.form.getlist("important_tasks")
        print(completed_tasks)
        print (tasks)
        for task in tasks:
            if str(task) in completed_tasks:
                print ("DONE")
                tasks.remove(task)
                Task.query.filter_by(name=task.name, date=current_date).delete()
                create_task(name=task.name, date=current_date, done=True)
        db.session.commit()
    return render_template('index_accueil.html', current_date=current_date, tasks = tasks, completed_tasks=completed_tasks, name=[d['first_name'], d['last_name']])


@app.route("/calendrier")
def calendrier():
    return render_template("calendrier.html")


@app.route("/recettes")
def recettes():
    return render_template("menu.html")


@app.route("/parametres")
def parametres():
    return "<h1>Paramètres</h1> <a href='/accueil'> Accueil </a> <br> <p>ici c'est pour gérer les paramètres ;)</p> <p> genre les notifs, le mot de passe ... </p>"


app.run()