from models.chat import Chat
from models.users import User


def find_user(id: int):
    user = User.query.filter_by(id=id)
    return user is not None


def get_list(id: int) -> list[Chat]:
    notify_list = Chat.query.filter_by(uid=id).all()
    return notify_list
