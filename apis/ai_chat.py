from flask import Blueprint,request
from services.get_message_response import get_message_response, get_image_response
from utils.Response import Response

chatAI_bp = Blueprint(name="ai_chat", import_name=__name__, url_prefix="/ai_chat")


@chatAI_bp.get("/<string:message>")
def get_response(message: str):
    image_base64 = request.args.get("image")
    if len(message) == 0:
        pass
    if image_base64:
        response = get_image_response(message, image_base64)
    else:
        response = get_message_response(message)
    return Response.success(data=response)

