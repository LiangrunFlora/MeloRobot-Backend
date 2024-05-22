from datetime import datetime

from extensions import db
from models.chat import Chat
from models.interaction import Interaction


def insert_interaction_message(
        message: str,
        message_type: int,
        u_message: str,
        uid: int,
        extension: str = "") -> Interaction:
    date_time = datetime.utcnow()
    if uid == -1:
        uid = 1
    interaction = Interaction(message=message,
                              message_type=message_type,
                              u_message=u_message,
                              uid=uid,
                              extension=extension,
                              time=date_time)
    db.session.add(interaction)
    db.session.commit()
    return interaction


def get_all_interaction_dao(id: int):
    chat = Chat.query.filter_by(id=id).first()
    print(chat)
    interaction_list = []
    if chat:
        interaction_id_string_list : str = chat.interaction_list
        interaction_id_list = interaction_id_string_list.split(" ")
        for interaction_id in interaction_id_list:
            interaction = Interaction.query.filter_by(id=interaction_id).first()
            if interaction:
                interaction_list.append(interaction.to_dict())
        return interaction_list
    else:
        return []


def update_chat_list(interaction_message, detail_id):
    chat = Chat.query.filter_by(id=detail_id).first()
    if chat:
        new_interaction_list = chat.interaction_list
        new_interaction_list += f" {interaction_message.id}"
        chat.interaction_list = new_interaction_list
        db.session.commit()
