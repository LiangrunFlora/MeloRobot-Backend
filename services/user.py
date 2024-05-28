from DAO.user import valid_user_account_password
from extensions import db
from models.users import User


def login_valid(account: str, password: str):
    user = valid_user_account_password(account, password)
    return user


def add_user(account: str, password: str, email: str):
    user = User.query.filter_by("email", email).first()
    if user:
        return None
    else:
        user = User(account=account,
                    password=password,
                    username=email,
                    email=email,
                    head_image="")
        db.session.add(user)
        db.session.commit()
        return user.to_dict()
