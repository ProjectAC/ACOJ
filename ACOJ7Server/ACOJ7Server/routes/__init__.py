from datetime import datetime
from flask import render_template
from ACOJ7Server import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html'
    )

from . import submission, user, test
