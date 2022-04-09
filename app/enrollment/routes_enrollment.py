from flask import Blueprint, render_template, url_for, redirect
from flask import current_app as app
from .forms_enrollment import *
from app.models import PlatformUser


# Blueprint Configuration
enrollment_bp = Blueprint(
    'enrollment_bp', __name__,
    template_folder='templates',
    static_folder='static'
)
