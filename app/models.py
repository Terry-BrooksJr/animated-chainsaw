from wtforms import StringField, SubmitField, PasswordField, RadioField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


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
        