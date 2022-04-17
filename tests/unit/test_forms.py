import pytest
from wtforms import StringField, SubmitField, DateField, PasswordField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
import string
import random
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import query
import json
from app.admin.forms_admin import CreatePlatformUser
import unittest 
import pytest

clean_file = open('/tests/unit/PlatformUsers-Clean.json')
dirty_file = open('/tests/unit/PlatformUsers-Dirty.json')





class TestForms():
    def vaild_temp_password(self,temp_password):
        temp_password = list(temp_password)
        bad_characters = list("$%&")
    
    
    def invalid_PlatformUser_username(username):
        pass
    
    for tp_char in temp_password:
        pass
        
#         if tp_char in bad_characters:
#         callsomefunction(i)
#         bad.append(i)
#     else:
#         newx.append(i)

# for i in y:
#     if i not in bad:
#         newy.append(i)


def vaild_PlatformUser_username(username):
    pass
    # data = json.load(clean_file)
    # for i in data['username']:
    #     if username == data[i]

    
    
    # for index, character in  temp_password:
    #     if character in bad_characters[i]
    #     assert character in temp_password != list("$%&") 


