from config.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(90), nullable=False)
    phone_number = db.Column(db.String)
    email = db.Column(db.String(90), unique=True, nullable=False)
    age = db.Column(db.String(90), nullable=True)
    password = db.Column(db.Text,nullable=True)

    def __init__(self, user_name, phone_number, email,age,password):
        self.user_name = user_name
        self.phone_number = phone_number
        self.email = email
        self.age = age
        self.password = password        
