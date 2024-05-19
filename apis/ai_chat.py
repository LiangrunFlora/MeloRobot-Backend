from flask import Blueprint
from utils.Response import Response

chatAI_bp = Blueprint(name="ai_chat", import_name=__name__, url_prefix="/ai_chat")



@chatAI_bp.get("/<string:message>")
def get_response(message):
    return Response.success()