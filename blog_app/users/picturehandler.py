import os
from PIL import Image
from flask import url_for, current_app


def profile_image(picture, username):
    filen = picture.filename
    filetype = filen.split('.')[-1]
    storing_name = str(username) + '.' + filetype
    filepath = os.path.join(current_app.root_path, 'static/pictures', storing_name)

    output_size = (500, 500)
    profile_picture = Image.open(picture)
    profile_picture.thumbnail(output_size)
    profile_picture.save()
    return storing_name
