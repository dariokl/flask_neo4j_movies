from flask import render_template

from . import static_bp as static

@static.route('/')
def home():

    return render_template ('index.html')