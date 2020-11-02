from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Email,EqualTo
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from blog_app.models import User
class Loginform(FlaskForm):
    email=StringField('enter email',validators=[DataRequired(),Email()])
    password=StringField('enter password',validators=[DataRequired()])
    submit=SubmitField('submit')

class Registerform(FlaskForm):
    username= StringField('enter username', validators=[DataRequired()])
    email = StringField('enter email', validators=[DataRequired(), Email()])
    password = StringField('enter password', validators=[DataRequired(),EqualTo('password2')])
    password2 = StringField('enter confirmed  password', validators=[DataRequired()])

    submit = SubmitField('submit')

    def check_email(self,field):
        if User.query.get(email=field.data).first():
            raise ValidationError('email already taken')
    def check_username(self,field):
        if User.query.get(username=field.data).first():
            raise ValidationError('username already taken')

class Updateform(FlaskForm):
    username = StringField('enter username', validators=[DataRequired()])
    email = StringField('enter email', validators=[DataRequired(), Email()])
    profile_picture=FileField('wanna update picture click here', validators=[FileAllowed(['jpg','png','jpeg'])])
    submit = SubmitField('submit')
    def check_email(self,field):
        if User.query.get(email=field.data).first():
            raise ValidationError('email already taken')
    def check_username(self,field):
        if User.query.get(username=field.data).first():
            raise ValidationError('username already taken')



