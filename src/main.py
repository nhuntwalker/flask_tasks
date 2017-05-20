"""Main python file for the app."""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def home_list():
    """View for listing out all of the tasks on deck."""
    return "This is the home list page"
