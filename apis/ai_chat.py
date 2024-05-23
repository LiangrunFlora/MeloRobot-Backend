from flask import Blueprint,request
from services.get_message_response import get_message_response, get_image_response, get_all_interaction, add_new_chat
from utils.Response import Response

chatAI_bp = Blueprint(name="ai_chat", import_name=__name__, url_prefix="/ai_chat")


@chatAI_bp.post("")
def get_response():
    data = request.json
    message = "注意：下面的问题使用简体中中来回答: " + data['message']+",别忘记使用简体中文回答。"
    image_base64 = data['image']
    uid = data['uid']
    detail_id = data['detail_id']
    print(detail_id)
    if uid is None:
        return Response.error(code=404, message="不存在当前帐号")
    else:
        if image_base64:
            print("进入base64")
            response = get_image_response(message, image_base64, uid=uid,  detail_id=detail_id)
        else:
            response = get_message_response(message, uid=uid, detail_id=detail_id)
        return response


@chatAI_bp.get("/<int:id>")
def get_chat_detail(id: int):
    if id:
        interaction_list = get_all_interaction(id)
        response = Response.success(data=interaction_list)
    else:
        response = Response.error(message="帐号不存在或登陆无效")
    return response


@chatAI_bp.post("/create")
def add_new():
    data = request.json
    uid = data.get("uid")
    title = data.get("title")
    notify = add_new_chat(uid, title)
    return Response.success(data=notify)
