# Imports
from flask import Flask

# Server declaration
app = Flask(__name__)

# Routes imports
import drive_routes
import dir_routes
import file_routes