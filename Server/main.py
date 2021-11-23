# Imports
from HTTPServer import app
from JSONHandler.loginHandler import *
from JSONHandler.fileHandler import *

# Server start
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)




