from extensions import db
from sqlalchemy.dialects.mysql import LONGTEXT


class Interaction(db.Model):
    __tablename__ = 'interaction'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(LONGTEXT, nullable=False)
    message_type = db.Column(db.Integer, nullable=False)  # 0: 文本, 1: 图片, 2: 文件
    u_message = db.Column(LONGTEXT, nullable=True)
    uid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, message, message_type, u_message, uid):
        self.message = message
        self.message_type = message_type
        self.u_message = u_message
        self.uid = uid

    def __repr__(self):
        return f'<Interaction {self.id}>'
