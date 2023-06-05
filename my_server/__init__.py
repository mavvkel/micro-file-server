from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = "data"
    app.config['SECRET_KEY'] = 'secret_key_goes_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes in the app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth routes in the app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    with app.app_context():
        db.create_all()

    return app
