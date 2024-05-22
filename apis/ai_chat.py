from flask import Blueprint,request
from services.get_message_response import get_message_response, get_image_response
from utils.Response import Response

chatAI_bp = Blueprint(name="ai_chat", import_name=__name__, url_prefix="/ai_chat")


@chatAI_bp.post("")
def get_response():
    data = request.json
    message = data['message']
    image_base64 = data['image']
    uid = data['uid']
    if uid is None:
        return Response.error(code=404, message="不存在当前帐号")
    else:
        if image_base64:
            response = get_image_response(message, image_base64)
        else:
            response = get_message_response(message, uid=uid)
        return response

