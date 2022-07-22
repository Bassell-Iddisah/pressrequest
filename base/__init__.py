from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_migrate import Migrate
from flask_loginmanager import LoginManager
from .config import Config

db = SQLAlchemy()
mail = Mail()
# migrate = Migrate()
loginmanager = LoginManager()
loginmanager.login_view = "user.signin"
loginmanager.login_message_category = "info"

def create_app(config=Config):
	app = Flask(__name__)
	db.init_app(app)
	mail.init_app(app)
	# migrate.init_app(app)
	loginmanager.init_app(app)
	from base.businesses.routes import bus
	app.register_blueprint(bus)
	return app
