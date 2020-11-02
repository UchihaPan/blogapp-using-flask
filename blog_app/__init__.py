from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask import Flask
from blog_app.main.views import main
from blog_app.error_handling.handers import error_handler
from flask_login import LoginManager

app = Flask(__name__)
basedirectory = os.path.abspath(os.path.dirname(__file__))
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedirectory, 'data.sqlite')
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy()
Migrate(app, database)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

app.register_blueprint(main)
app.register_blueprint(error_handler)
