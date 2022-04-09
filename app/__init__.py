from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from config import Config


# Globally accessible libraries
db = SQLAlchemy()
r = FlaskRedis()
login_manager = LoginManager()


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)
    login_manager.init_app(app)


    with app.app_context():
        # Include our Routes
        from app.login import routes_login
        from app.admin import routes_admin
        from app.dashboard import routes_dashboard
        from app.enrollment import routes_enrollment

        # Register Blueprints
        app.register_blueprint(routes_login.login_bp)
        app.register_blueprint(routes_admin.admin_bp)
        app.register_blueprint(routes_dashboard.dashboard_bp)
        app.register_blueprint(routes_enrollment.enrollment_bp)

        return app