from django.forms import ValidationError
from wtforms import StringField, SubmitField, PasswordField, BooleanField,Flags
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from flask_login import UserMixin
from flask_rbac import RoleMixin

class PlatformUser(UserMixin):
    def __init__(self, username, user_id, user_first_name, user_last_name, role, password, care_facility, date_account_created, last_date_modified, is_active, last_logged_in):
        self.username = username
        self.user_id = user_id
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.password = password
        self.care_facility = care_facility
        self.date_account_created = date_account_created
        self.last_date_modified = last_date_modified
        self.is_active = is_active
        self.role = role
        self.last_logged_in = last_logged_in
        
        if (username, user_id, user_first_name, user_last_name, password, care_facility, date_account_created, role) == None or '':
            raise In
        if not isinstance(user_first_name or user_last_name or role or username, str):
            raise ValueError("Invaild Data Type - User's Name, Role, and username must be a string")
        if not isinstance(user_id, int) and (len(username) > 8):
            raise ValueError("Invalid User ID. User ID must be all intergers not exceeding 8 characters")
    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
    def check_password(self, password):
        return bcrypt.checkpw(password, password_hash)
        return check_password_hash(self.password_hash, password)
    def is_active(self):
        return super().is_active()
    def is_authenticated(self):
        return super().is_authenticated
    def is_anonymous(self):
        return super().is_anonymous
    def validate_unique_username(self,username):
        username = PlatformUser.object(username=username.data).first()
        if username:
            raise ValidationError("{} is unavailable. Please select a new username.format(request.form['username'])");


class Role(RoleMixin):
    pass


anonymous = Role('anonymous')
class PlatformUser:
    def __init__(self, username, user_id, user_first_name, user_last_name, role, password, care_facility, date_account_created, last_date_modified, is_active, last_logged_in):
        self.username = username
        self.user_id = user_id
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.password = password
        self.care_facility = care_facility
        self.date_account_created = date_account_created
        self.last_date_modified = last_date_modified
        self.is_active = is_active
        self.role = role
        self.last_logged_in = last_logged_in
        