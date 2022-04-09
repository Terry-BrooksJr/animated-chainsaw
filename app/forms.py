from wtforms import StringField, SubmitField, PasswordField,RadioField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Please Enter Vaild Username')])
    password = PasswordField('Password', validators = [DataRequired(message = 'Please Enter Vaild Password')])
    remember_me = RadioField('Remember Me?')
    submit = SubmitField('Login')
