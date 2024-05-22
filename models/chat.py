from extensions import db


class Chat(db.Model):
    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    interaction_list = db.Column(db.Text, nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)

    def __init__(self, interaction_list, uid, title):
        self.interaction_list = interaction_list
        self.uid = uid
        self.title = title

    def __repr__(self):
        return f'<Chat {self.id}>'
