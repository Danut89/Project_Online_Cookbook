import os
from flask import current_app
from werkzeug.utils import secure_filename

def save_uploaded_image(image):
    """
    Save an uploaded image to the configured upload folder.

    Args:
        image: The uploaded image file (via Flask-WTF).

    Returns:
        str: The relative URL path of the saved image.
    """
    if not image:
        return None

    # Secure the filename
    filename = secure_filename(image.filename)
    upload_folder = current_app.config['UPLOAD_FOLDER']
    image_path = os.path.join(upload_folder, filename)

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    # Save the image
    image.save(image_path)

    # Return the relative URL path
    return f"/static/uploads/{filename}"
