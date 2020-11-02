from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask import Flask
from blog_app.main.views import main
from blog_app.error_handling.handers import error_handler

app = Flask(__name__)
basedirectory = os.path.abspath(os.path.dirname(__file__))
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedirectory, 'data.sqlite')
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy()
Migrate(app, database)

app.register_blueprint(main)
app.register_blueprint(error_handler)
