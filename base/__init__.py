from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app(config=Config):
	app = Flask(__name__)
	db.init_app(app)
	from businesses.routes import bus
	app.register_blueprint(bus)
	return app
