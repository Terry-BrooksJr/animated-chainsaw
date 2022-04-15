from django.forms import ValidationError
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class PlatformUser(UserMixin):
    def __init__(self, username, user_id, user_first_name, user_last_name, role, password, care_facility, date_account_created, last_date_modified, is_active, last_logged_in,):
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
    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def is_active(self):
        return super().is_active()
    def is_authenticated(self):
        return super().is_authenticated
    def is_anonymous(self):
        return super().is_anonymous
    def validate_unique_username(self.username):
        username = PlatformUser.object(username=username.data).first()
        if username:
            raise ValidationError(f'{username) is unavailable. Please select a new username.');

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
        