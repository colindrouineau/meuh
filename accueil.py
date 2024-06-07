from flask import Flask, request, render_template
from datetime import datetime 
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from sqlalchemy import select


app = Flask("MEUUUHH_accueil")
static_folder = 'static'

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
db.init_app(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
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

@app.route("/", methods=["GET", "POST"])
def accueil():
    #current_date = datetime.now().strftime("%d-%m-%Y")
    current_date = datetime.now().date()
    print (current_date)
    tasks= Task.query.filter_by(date=current_date).all() 
    print(tasks)
    #fonctionne pas car prend en compte date +heure je pense...
    if request.method == "POST":
        for task in tasks:
            if task.done == True:
                tasks.remove(task)
                Task.query.filter_by(name=task.name, date=current_date).delete()
                create_task(name=task.name, date=current_date, done=True)
        db.session.commit()
    return render_template('index_accueil.html', current_date=current_date, tasks = tasks)


@app.route("/calendrier")
def calendrier():
    return render_template("calendrier.html")


@app.route("/recettes")
def recettes():
    return render_template("menu.html")


@app.route("/parametres")
def parametres():
    return "<h1>Paramètres</h1> <a href='/'> Accueil </a> <br> <p>ici c'est pour gérer les paramètres ;)</p> <p> genre les notifs, le mot de passe ... </p>"


app.run(debug=False, port = 3000)


