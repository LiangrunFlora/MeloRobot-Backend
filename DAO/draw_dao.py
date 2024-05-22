import json

from models.dialog_list import DialogList
from models.draw_content import DrawContent
from models.interaction import Interaction
from extensions import db

"""
    for table draw_content
"""


def insert_draw_content(url, uid, text, dialog_id):
    new_draw_content = DrawContent(url=url, uid=uid, text=text, dialog_id=dialog_id)
    db.session.add(new_draw_content)
    db.session.commit()

    return new_draw_content


def get_all_draw_content(dialog_id):
    responses = DrawContent.query.filter_by(dialog_id=dialog_id).all()
    draw_contents = [json.dumps(item.to_dict()) for item in responses]

    return draw_contents


"""
    for table dialog_list
"""


def insert_dialog(uid, title, message_list=""):
    new_dialog = DialogList(uid=uid, message_list=message_list, title=title)
    db.session.add(new_dialog)
    db.session.commit()

    return new_dialog


def update_dialog(id, message_list):
    dialog = DialogList.query.filter_by(id=id).first()
    dialog.message_list = message_list
    db.session.commit()


def get_all_dialog(uid):
    return DialogList.query.filter_by(uid=uid).all()


