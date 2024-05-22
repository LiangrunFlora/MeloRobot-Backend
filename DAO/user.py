from models.users import User


def valid_user_account_password(account: str, password: str):
    user = User.query.filter_by(account=account, password=password).first()
    if user:
        return user.to_dict()
    else:
        return None
