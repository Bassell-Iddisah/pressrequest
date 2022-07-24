from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_migrate import Migrate
# from flask_loginmanager import LoginManager
from .config import Config

# db = SQLAlchemy()
mail = Mail()
# migrate = Migrate()
# loginmanager = LoginManager()
# loginmanager.login_view = "user.signin"
# loginmanager.login_message_category = "info"

def create_app(config=Config):
	app = Flask(__name__)
	app.config.from_object(Config)
	# db.init_app(app)
	mail.init_app(app)
	# migrate.init_app(app)
	#loginmanager.init_app(app)
	from base.main.routes import main
	from base.businesses.routes import bus
	from base.users.routes import user
	app.register_blueprint(main)
	app.register_blueprint(bus)
	app.register_blueprint(user)
	return app
