from flask import Blueprint,request

from services.notify import get_notify_list
from utils.Response import Response

notify_bp = Blueprint(name="notify", import_name=__name__, url_prefix="/get_notify")


@notify_bp.get("/<int:id>")
def notify_list_get(id: int):
    notify_list = get_notify_list(id)
    return Response.success(data=notify_list)

