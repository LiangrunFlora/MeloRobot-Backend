from extensions import db
from sqlalchemy.dialects.mysql import LONGTEXT


class Interaction(db.Model):
    __tablename__ = 'interaction'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(LONGTEXT, nullable=False)
    extension = db.Column(LONGTEXT, nullable=True)
    message_type = db.Column(db.Integer, nullable=False)  # 0: 文本, 1: 图片, 2: 文件
    u_message = db.Column(LONGTEXT, nullable=True)
    uid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, message: object, message_type: object, u_message: object, uid: object, extension: object) -> object:
        self.message = message
        self.message_type = message_type
        self.u_message = u_message
        self.uid = uid
        self.extension = extension

    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "message_type": self.message_type,
            "u_message": self.u_message,
            "uid": self.uid,
            "extension": self.extension
        }

    def __repr__(self):
        return f'<Interaction {self.id}>'
