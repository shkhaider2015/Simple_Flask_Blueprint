from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from myApp.config import Config


db = SQLAlchemy()

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    db = SQLAlchemy()

    from myApp.main.routes import main

    
    app.register_blueprint(main)

    return app