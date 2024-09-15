from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120),nullable=False)

    def __init__(self, username, password,email):
        self.username = username
        self.set_password(password)
        self.email=email

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'email':self.email
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def editUsername(self,username):
        self.username=username

    def editPassword(self,password):
        self.password=password
        
    def editEmail(self,email):
        self.email=email

    def addExercise(self):
    
    def completeExercise(self):
    
    def signUp(self,username,email,password):
    
    def login(self,email,password):

        if check_password(password):
            return true
        return false