from flask import Flask, request, render_template

app = Flask("MEUUUHH")

@app.route("/")
def index():
    return render_template("index_resan.html")

@app.route("/Connexion")
def about():
    return "<h1>Connexion</h1> <a href='/'> Accueil </a> <br> <p>ici vous pourrez vous connecter à votre compte ;)</p>"

@app.route("/Inscription")
def info():
    return "<h1>Inscription</h1> <a href='/'> Accueil </a> <br> <p>ici vous pourrez vous inscrire le premier jour !</p>"


app.run(debug=False, port = 4000)

