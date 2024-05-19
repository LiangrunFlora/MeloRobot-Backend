from extensions import db


class DrawContent(db.Model):
    __tablename__ = 'draw_content'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    text = db.Column(db.Text, nullable=True)
    dialog_id = db.Column(db.Integer, db.ForeignKey('dialog_list.id'), nullable=False)

    def __init__(self, url, uid, text, dialog_id):
        self.url = url
        self.uid = uid
        self.text = text
        self.dialog_id = dialog_id

    def __repr__(self):
        return f'<DrawContent {self.id}>'
