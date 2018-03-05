import os

from flask import Flask
app = Flask(__name__)   # this just to make sure you have an unique instance for that flask app

@app.route('/')
def hello_world():
    return 'Hello World!'
    
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0') # this will define the preset environment variable to an IP
    port = int(os.getenv('PORT', 5000))
    app.run(host = host, port = port)