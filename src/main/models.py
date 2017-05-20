"""Model module for the Flask app."""
from main.app_config import db
from datetime import datetime


class Task(db.Model):
    """The Task model for this app."""

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode)
    description = db.Column(db.Unicode)
    completed = db.Column(db.Boolean, default=False)
    datetime = db.Column(db.DateTime)

    def __init__(self, *args, **kwargs):
        """A slight modification to the Task constructor."""
        super(Task, self).__init__(*args, **kwargs)
        self.datetime = datetime.now()

    def __repr__(self):
        """String representation of the model."""
        return f"<Task {self.id} - {self.title}>"
