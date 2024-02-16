import flask
import sqlalchemy
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from flask_wtf import FlaskForm #pour la partie qui fonctionne pas

#initialisation des databases
db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

#le site de base
@app.route('/')
def site():
    return 'BAAAAAAA'

#essai d'une autre page
@app.route('/home')
def home():
    return 'Home'

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

@app.route('/index')
def index():
    students = User.query.all()
    return render_template('index.html', students=students)

@app.route('/essai')
def essai():
    return "essai"

if __name__ == '__main__':
    app.run()

#crée un user 'admin' dans la database
with app.app_context():
    db.create_all()
    db.session.commit()
    create_user('admin', '.', 'admin')



'''
#ce que copilot a proposé, mais ça fonctionne pas encore
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('site'))
    return render_template('register.html', title='Register', form=form)
'''