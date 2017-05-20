"""Main python file for the app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS', ''))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def home_list():
    """View for listing out all of the tasks on deck."""
    return "This is the home list page"

if __name__ == "__main__":
    app.run()
