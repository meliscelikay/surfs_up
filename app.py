# Import the Flask dependencies
from flask import Flask
# Create a new Flask app instance
app = Flask(__name__)
#define the starting point/root
@app.route('/')
# Create Flask Routes
def hello_world():
    return 'Hello world'