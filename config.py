import os
import cloudinary

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CLOUDINARY_CLOUD_NAME = os.getenv('dweokknym')
    CLOUDINARY_API_KEY = os.getenv('1519767986386474')
    CLOUDINARY_API_SECRET = os.getenv('3AONECiEjbbXI-3uyskxKLsy6xQ')

 # Upload folder for recipe images
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app', 'static', 'uploads')# ✅ Upload folder fix
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app', 'static', 'uploads')
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "WEBP"}

    

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)