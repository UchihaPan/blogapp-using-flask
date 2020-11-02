from blog_app import database


class user:
    __tablename__ = 'users'
    id = database.column(database.Integer, primary_key=True)
    profile = database.column(database.String(20), nullable=False, defalult='a.jpg')
