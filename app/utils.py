import os
from flask import current_app
from werkzeug.utils import secure_filename

def save_uploaded_image(image):
    """
    Save an uploaded image to the static/uploads directory.
    """
    if not image:
        return None

    # Secure filename
    filename = secure_filename(image.filename)

    # Absolute path to /static/uploads
    upload_path = os.path.join(current_app.root_path, 'static', 'uploads', filename)

    # Create folder if needed
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)

    # Save the image
    image.save(upload_path)

    # Return the path used in templates
    return f"/static/uploads/{filename}"
