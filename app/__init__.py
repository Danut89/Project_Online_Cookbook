from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf import CSRFProtect
import cloudinary
import os
from dotenv import load_dotenv
from flask import render_template

if os.getenv("RENDER") is None:  # Only load .env locally
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
    from app.models import User

    # Define Flask-Login user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route("/create-default-categories")
    def create_default_categories():
        try:
            from app.models import Category  # adjust to your actual Category model name

            default_categories = [
                "Breakfast", "Lunch", "Dinner", "Snack", "Dessert", "Vegan", "Vegetarian"
            ]

            for name in default_categories:
                # only add if it doesn’t already exist
                if not Category.query.filter_by(name=name).first():
                    c = Category(name=name)
                    db.session.add(c)

            db.session.commit()
            return "✅ Default categories added successfully!"
        except Exception as e:
            return f"❌ Error: {str(e)}"


    # Import and register blueprints AFTER app is created
    from app.routes import main
    from app.auth import auth

    cloudinary.config(
        cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
        api_key=os.getenv("CLOUDINARY_API_KEY"),
        api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    )

    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix="/auth")

    # Error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(403)
    def forbidden_error(e):
        return render_template("errors/403.html"), 403

    return app
