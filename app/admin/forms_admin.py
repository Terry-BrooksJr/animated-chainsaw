from wtforms import StringField, SubmitField, DateField, PasswordField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
import string
import random
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

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
        """
        It creates a random password of length 12, with at least one uppercase letter, one lowercase letter,
        one digit, and one special character
        :return: A string of 12 characters, with at least one uppercase letter, one lowercase letter, one
        digit, and one special character.
        """
        alphabets = list(string.ascii_letters)
        digits = list(string.di2gits)
        special_characters = list("!@*()")
        characters = list(string.ascii_letters + string.digits + "!@#*()")
        password = []
        for i in range(random.randint(0, 10)):
            password.append(random.choice(alphabets))
        for i in range(digitrandom.randint(0, 4)):
            password.append(random.choice(digits))
        for i in range(random.randint(0, 2)):
            password.append(random.choice(special_characters))
        if len(password) < 12:
            random.shuffle(characters)
            for i in range(12 - len(password)):
                password.append(random.choice(characters))
        elif len(password) > 12:
            password = password[0:13]
            random.shuffle(password)
        return("".join(password))
    
