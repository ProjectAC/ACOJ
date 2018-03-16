"""
The flask application package.
"""

from ACOJ7Server.privacy import sessionKey
from flask import Flask
app = Flask(__name__)

app.secret_key = sessionKey

import ACOJ7Server.views
