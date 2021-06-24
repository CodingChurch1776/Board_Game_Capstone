from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
import uuid # stands for unique user identifier 

#Adding Flask Security for password protection - comes built in with flask
from werkzeug.security import generate_password_hash, check_password_hash


import secrets


from flask_login import UserMixin, LoginManager


from flask_marshmallow import Marshmallow



db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    username = db.Column(db.String(64), nullable = False, default = '')
    email = db.Column(db.String(120), nullable = False)
    password = db.Column(db.String(128), nullable = False, default = '')
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, username, first_name = '', last_name = '', id = '', password = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.username = username




    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def set_username(self, username):
        return self.username
        
    def __repr__(self):
        return '<User {}>'.format(self.username) 

class Game(db.Model):
    name = db.Column(db.String(150), nullable = False, default = '', primary_key = True)
    year = db.Column(db.String(150), nullable = True, default = '')
    rating = db.Column(db.Integer, nullable = True, default = '')
    designer = db.Column(db.String(150), nullable = True, default = '')
    genre = db.Column(db.String(150), nullable = True, default = '')
    
    def __init__(self, name, year, rating, designer, genre):

        self.name = name
        self.year = year
        self.rating = rating
        self.designer = designer
        self.genre = genre

    def __repr__(self):
        return f'The following board game has been added to your collection: {self.name}'
    
class GameSchema(ma.Schema):
    class Meta:
        fields = ['name', 'year', 'rating', 'designer', 'genre']

game_schema = GameSchema()

game_schemas = GameSchema(many = True)




