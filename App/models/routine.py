from App import db

class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    exercises = db.relationship('Exercise', secondary=routine_exercise, back_populates='routines')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)





routine_exercise = db.Table('routine_exercise',
    db.Column('routine_id', db.Integer, db.ForeignKey('routine.id')),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id')),
    db.PrimaryKeyConstraint('routine_id', 'exercise_id')
)