# App/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Add your app configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    
    # Initialize the database with the app
    db.init_app(app)

    # Import models, views, etc., after app is created
    from .models import user
    from .views import some_view

    # Register Blueprints or other app components
    # app.register_blueprint(some_blueprint)

    return app










# from .models import *
# from .views import *
# from .controllers import *
# from .main import *
