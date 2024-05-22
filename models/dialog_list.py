from extensions import db
from dataclasses import dataclass


@dataclass
class DialogList(db.Model):
    __tablename__ = 'dialog_list'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message_list = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)

    def __init__(self, uid, message_list, title):
        self.uid = uid
        self.message_list = message_list
        self.title = title

    def __repr__(self):
        return f'<DialogList {self.id}>'
