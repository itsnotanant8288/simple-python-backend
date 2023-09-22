from config.db import db

class SUClass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String, nullable=False)
    stu_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, default=None)

    def __init__(self, class_name, stu_id, user_id=None):
        self.class_name = class_name
        self.stu_id = stu_id
        self.user_id = user_id
