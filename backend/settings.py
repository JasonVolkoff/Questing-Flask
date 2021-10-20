from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

app = Flask(__name__, static_folder="../frontend/dist", template_folder="../frontend")

# TODO: Change these to exported environment variables
POSTGRES_USER = ''
POSTGRES_PASSWORD = ''
POSTGRES_DATABASE_NAME = ''
DEVELOPMENT = False

# Import Settings
try:
    from local_settings import *
except ImportError:
    pass

# Database Config Settings
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost/{POSTGRES_DATABASE_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Migration Settings
migrate = Migrate(app, db)

def create_db():
    """
    Creates the db tables.
    TODO: Make functional app-factory
    """
    db.create_all()


# Routing
from urls import *

