import os
from PIL import Image
from flask import current_app
import uuid


def add_featured_image(upload_image):
    # image_filename = upload_image.filename
    image_filename = str(uuid.uuid4()) + os.path.splitext(upload_image.filename)[1]
    filepath = os.path.join(current_app.root_path, r"static/featured_image", image_filename)
    image_size = (600, 600)
    image = Image.open(upload_image)
    image.thumbnail(image_size)
    image.save(filepath)
    return image_filename
