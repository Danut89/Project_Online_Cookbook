from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf import CSRFProtect
import cloudinary
import os
from dotenv import load_dotenv

# ✅ Load environment variables from .env file
load_dotenv()

csrf = CSRFProtect()


# Initialize Flask extensions
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "auth.login"  # Redirects to login page if user is not logged in

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize extensions with app
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Import models BEFORE using them
    from app.models import User  # ✅ FIX: Moved import up

    # Define Flask-Login user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import and register blueprints AFTER app is created
    from app.routes import main
    from app.auth import auth

    cloudinary.config(
        cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
        api_key=os.getenv("CLOUDINARY_API_KEY"),
        api_secret=os.getenv("CLOUDINARY_API_SECRET")
    )



    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix='/auth')

    return app


