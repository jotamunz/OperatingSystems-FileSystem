# Imports
from flask import Flask

# Server declaration
app = Flask(__name__)

# Routes imports
import HTTPServer.drive_routes
import HTTPServer.dir_routes
import HTTPServer.file_routes