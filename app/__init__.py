from flask import Flask

app = Flask(__name__, static_folder='static')

from app import routes
from app import pages_data
