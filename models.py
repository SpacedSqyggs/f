from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin): 
    id = db.Column(db.Interger, primary_key=True)
    email = db.Coloumn(db.String(150), unqiue=True)
    password= db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True)