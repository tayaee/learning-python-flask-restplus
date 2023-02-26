from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name='dev'):
    app = Flask(__name__) # ???
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    migrate = Migrate(app, db)
    return app
