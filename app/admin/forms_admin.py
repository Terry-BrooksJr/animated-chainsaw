from wtforms import StringField, SubmitField, DateField, PasswordField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
import string
import random
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import os

# from wtforms.ext.sqlalchemy.orm import model_form

from app.models import PlatformUser

platform_user_roles = ['Admin']
class CreatePlatformUser(FlaskForm):
    user_first_name = StringField("New User's First Name", validators=[InputRequired()])
    user_last_name = StringField("New User's Last Name",  validators=[InputRequired()])
    daycare_facility = StringField("Primary Daycare Location", validators=[InputRequired()])
    role = BooleanField("Check to grant the new user administrative privileges?")
    
    # def create_username(self, user_first_name, user_last_name):
    #     username = (user_first_name[0:1] + user_last_name)
    #     while username == PlatformUser.query.filter_by(username=username).first():
    #         username = username + str((random.randint(0, 250)))
    #     return username 
        #         username =
        # try:
        #     username = (user_first_name[0:1] + user_last_name)
        #     return username
        # except: 
        #     if username == PlatformUser.query.filter_by(username=username).first():
        #         username = username + str((random.randint(0, 250)))
        #         username = 
             
    
    def create_temp_password(self):
        length = 13
        chars = string.ascii_letters + string.digits + '!@#$%^&*()';
        random.seed = (os.urandom(1024));
        print ''.join(random.choice(chars) for i in range(length));
    
