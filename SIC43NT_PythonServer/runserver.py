"""
This script runs the SIC43NT_PythonServer application using a development server.
"""

from os import environ
from SIC43NT_PythonServer import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
