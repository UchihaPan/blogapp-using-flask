from flask import Flask

app = Flask(__name__)
from blog_app.main.views import main

app.register_blueprint(main)
