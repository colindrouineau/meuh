import flask
from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_sqlalchemy import SQLAlchemy

#initialisation des databases
db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

#variables globales (temporaire)
FIRST_NAME = ''
LAST_NAME = ''

d={'first_name':FIRST_NAME, 'last_name':LAST_NAME}

#inscription
@app.route('/', methods=['GET', 'POST'])
def signup():
    form=MyForm(request.form)
    if form.submit.data:
        d['first_name']=form.first_name.data
        d['last_name']=form.last_name.data
        with app.app_context():
            db.create_all()
            db.session.commit()
            create_user('baba', 'raaa')
        return redirect(url_for('home'))
    return render_template('signup.html', form=form)

@app.route('/home')
def home():
    return (d['first_name'] + ' ' + d['last_name'])

class MyForm(Form):
    first_name = StringField('First Name')
    last_name  = StringField('Last Name')
    submit = SubmitField('Submit') 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

def create_user(first_name, last_name):
    user = User(username=first_name, email=last_name)
    db.session.add(user)
    db.session.commit()

app.run()