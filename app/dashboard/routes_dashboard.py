from flask import Blueprint, render_template, url_for, redirect
from flask import current_app as app
from flask_login import login_required


# Blueprint Configuration
dashboard_bp = Blueprint(
    'dashboard_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('homepage.jinja',
                           title='Safari Life Child Management System - Login',
                           template='base',
                           location = "homepage")