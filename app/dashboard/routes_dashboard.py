from flask import Blueprint, render_template, url_for, redirect
from flask import current_app as app


# Blueprint Configuration
dashboard_bp = Blueprint(
    'dashboard_bp', __name__,
    template_folder='templates',
    static_folder='static'
)
