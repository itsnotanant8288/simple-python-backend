from config.db import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    class_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, default=None)
    age = db.Column(db.String(90), nullable=True)

    def __init__(self, name, class_id,age, user_id=None):
        self.name = name
        self.class_id = class_id
        self.user_id = user_id
        self.age = age

