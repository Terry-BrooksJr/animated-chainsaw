from flask import Blueprint, render_template, url_for, redirect
from flask import current_app as app
from .forms_admin import *


# Blueprint Configuration
admin_bp = Blueprint(
    'admin_bp', __name__,
    template_folder='templates',
    static_folder='static'
)
