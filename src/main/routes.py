"""Main python file for the app."""
from main import app


@app.route('/')
def home_list():
    """View for listing out all of the tasks on deck."""
    return "This is the home list page"

