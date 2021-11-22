# Imports
from HTTPServer import app
from JSONHandler.loginHandler import *
from JSONHandler.fileHandler import *


# print(getDirContent("Soap/root/folder1/subfolder1/t"))

# Server start
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)




