from datetime import datetime
from todoproject import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    due = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Todo('{self.id}', '{self.due}', '{self.state}', '{self.description}')"