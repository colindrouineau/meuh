from flask import Flask, request
app=Flask(__name__)

@app.route('/')
def index():#convention pour la page d'accueil
    return "<h1>BAAAAAAA</h1> <a href='/about'>About</a>"

#les deux solutions suivantes permettent de faire à peu près la même chose
@app.route('/hello')
def hello():
    #si on rajoute ?name=quelquechose, ça rajoute quelquechose dans le message
    name= request.args.get('name', 'No Name') #'No Name' est la valeur par défaut
    return f"<h1>Hello, {name}</h1>"

@app.route('/user/<string:name>/<int:repeat>') #on peut mettre int, float, path, etc. pour préciser le type
def user_profile(name, repeat):
    return f"<h1>User: {name}</h1>" *repeat

@app.route('/about')
def about():
    return '<h1>About</h1> <br> <p>bleu</p>'
app.run()