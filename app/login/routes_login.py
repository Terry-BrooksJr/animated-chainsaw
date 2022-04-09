from app.models import PlatformUser
from flask import flash, redirect, render_template, request, url_for, Blueprint, current_app as app
from flask_login import UserMixin, current_user,login_user, LoginManager
from .forms_login import LoginForm

login_manager = LoginManager()
login_manager.init_app(app)
# Blueprint Configuration
login_bp = Blueprint(
    'login_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@login_bp.route('/', methods=['GET', 'POST'])
@login_bp.route('/')
@login_bp.route('/home')
def login():
    form = LoginForm(csrf_enabled=False)
    return render_template(
        'login.html.jinja2',
        title='Safari Life Child Management System - Login',
        template='login',
        form=form)


@login_manager.user_loader
def load_user(user_id):
    return PlatformUser.query.get(int(user_id))

@login_bp.route('/authorize_user', methods=['POST'])
def verify_user():
    """login flow"""
    form = LoginForm(csrf_enabled=False)
    test_user = form.password.data
    test_pass = form.username.data
    if form.validate_on_submit():
        if test_pass == 'Testing':
            if test_user == 'TestUser':
                login_user(PlatformUser, remember=form.remember_me.data)
                return redirect(url_for('dashboard'), title='Safari Life Child Management System - Homepage', form=form, template='dashboard-template', _external=True, _scheme='https')
        # user = PlatformUser.query.filter_by(username=form.username.data).first()
        # if user and PlatformUser.check_password(form.password.data):
        else:
            flash(f'The username {{form.username.data}} and the provided password combination is not in our system.\n Please check the credentials provided and reattempt your login', 'danger' )            
            return redirect(url_for('login', _external=True, _scheme='https'))


