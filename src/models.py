"""Model module for the Flask app."""
from main.db import (
    Model, Column,
    Integer, Unicode,
    Boolean, DateTime
)
from datetime import datetime


class Task(Model):
    """The Task model for this app."""

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    description = Column(Unicode)
    completed = Column(Boolean, default=False)
    datetime = Column(DateTime)

    def __init__(self, *args, **kwargs):
        """A slight modification to the Task constructor."""
        super(Task, self).__init__(*args, **kwargs)
        self.datetime = datetime.now()

    def __repr__(self):
        """String representation of the model."""
        return f"<Task {self.id} - {self.title}>"
