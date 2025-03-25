import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

 # Upload folder for recipe images
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app', 'static', 'uploads')# ✅ Upload folder fix
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app', 'static', 'uploads')
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "WEBP"}