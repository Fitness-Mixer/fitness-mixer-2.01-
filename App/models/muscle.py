from App import db

class Muscle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    exercises = db.relationship('Exercise', secondary='exercise_muscle', back_populates='muscles')


exercise_muscle = db.Table('exercise_muscle',
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id')),
    db.Column('muscle_id', db.Integer, db.ForeignKey('muscle.id'))
)