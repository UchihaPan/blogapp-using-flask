from blog_app import database
from werkzeug import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class User(database.Model, UserMixin):
    __tablename__ = 'users'
    id = database.column(database.Integer, primary_key=True)
    profile = database.column(database.String(20), nullable=False, defalult='a.jpg')
    username = database.column(database.String(64), unique=True, index=True)

    email = database.column(database.String(64), unique=True, index=True)
    password_hash = database.column(database.String(64))

    posts = database.relationship('posts', backref='bhaibhai', lazy=True)

    def __init__(self, username, email, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
