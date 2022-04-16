from re import template
from app.models import PlatformUser
from flask import flash, redirect, render_template, request, url_for, Blueprint, current_app as app,g, session 
from flask_login import UserMixin, current_user,login_user, LoginManager
from .forms_login import LoginForm
from flask_wtf.csrf import CSRFError
from app import redirect_back, is_safe_url, get_redirect_target



login_bp = Blueprint(
    'login_bp', __name__,
    template_folder='templates',
    static_folder='static'
)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#Helper Function
#* Functions to support login/logout flow


# Blueprint Configuration
# * Need the these for for flask-login
@login_manager.user_loader
def load_user(user_id):
    return PlatformUser.query.get(int(user_id))

# * Looks for Previous USER Sessions and sets the global USER ID to the found value or NONE
@login_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@login_bp.route('/', methods=['GET', 'POST'])
@login_bp.route('/')
@login_bp.route('/home')
def login():
    form = LoginForm()
    username = form.username.data
    return render_template(
        'login.html.jinja',
        title='Safari Life Child Management System - Login',
        template='login',
        form=form, username = username)


@login_bp.route('/authorize_user', methods=['POST'])
def verify_user():
    """login flow"""
    form = LoginForm()
    if form.validate_on_submit():
        username = form.password.data  # ! Temporary - Need it for Testing
        password = form.username.data # ! Temporary - Need it for Testing
        user = PlatformUser.object(user_id=user_id).first() 
        if user == 'Testing' and test_user == 'TestUser':
            login_user(PlatformUser)
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('dashboard_bp.dashboard'), title='Safari Life Child Management System - Homepage', form=form, template='dashboard-template', _external=True, _scheme='https')
        # user = PlatformUser.query.filter_by(username=form.username.data).first() #TODO:Uncomment out lines 44 & 45 when Database is set 
        # if user and PlatformUser.check_password(form.password.data):
        else:
            flash(f'The username {test_user} and the provided password combination is not in our system.\n Please check the credentials provided and reattempt your login', 'danger' )            
            return redirect(url_for('login_bp.login', _external=True, _scheme='https'))



@login_bp.route('/logout')
def logout():
    session.clear()
    flash('You have successfully logged out! See Ya Later')
    return redirect(url_for('login'))


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description, title='Security Error', template='base'), 400


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', 404, title='Page Not Found', template='base')


