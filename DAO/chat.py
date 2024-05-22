from extensions import db
from models.interaction import Interaction


def insert_interaction_message(
        message: str,
        message_type: int,
        u_message: str,
        uid: int,
        extension: str = "") -> Interaction:
    if uid == -1:
        uid = 1
    interaction = Interaction(message=message,
                              message_type=message_type,
                              u_message=u_message,
                              uid=uid,
                              extension=extension)
    db.session.add(interaction)
    db.session.commit()
    return interaction
