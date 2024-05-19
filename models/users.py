from extensions import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    head_image = db.Column(db.String(200))

    def __init__(self, account, password, username, email, head_image=None):
        self.account = account
        self.password = password
        self.username = username
        self.email = email
        self.head_image = head_image

    def __repr__(self):
        return f'<User {self.username}>'