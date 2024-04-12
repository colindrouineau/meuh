from flask import Flask, request, render_template
from datetime import datetime 

app = Flask("MEUUUHH_accueil")
static_folder = 'static'


@app.route("/")
def accueil():
    current_date = datetime.now().strftime("%d-%m-%Y")
    tasks = ["task_1", "task_2", "task_3"]
    # il faudrait trouver un moyen d'ajouter les tasks de la journée en fonction de la journée
    # et updater les tasks tous les jours, en les reliant à la base de données ?
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


