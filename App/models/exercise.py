from App.database import db

class Exercise(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False, unique=True)
    category = db.Column(db.String(120),nullable=False)
    difficulty = db.Column(db.String(120),nullable=False)
    Equipment = db.Column(db.String(120),nullable=False)

    
