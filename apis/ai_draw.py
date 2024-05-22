from flask import request
from flask import Blueprint
from services import draw_service
from utils.Response import Response
from utils.draw_utils import styles
import asyncio

drawAI_bp = Blueprint(name="ai_draw", import_name=__name__, url_prefix="/draws")


@drawAI_bp.route("/", methods=["POST"])
def initial_chat():
    """
        uid: 本次聊天用户的id
        title: 本次聊天的标题
    """
    uid = request.json.get("uid")
    title = request.json.get("title")

    draw_service.new_draw_chat(uid, title)
    return Response.success(200, "初始化绘画对话成功")


@drawAI_bp.route("/image", methods=["POST"])
def text_convert_image():
    """
        uid: 本次聊天用户的id
        text: 用户输入的文本
        dialog_id: 本次聊天的id
    """
    uid = request.json.get("uid")
    text = request.json.get("text")
    dialog_id = request.json.get("dialog_id")
    draw_style = "探索无限"

    for style in styles:
        if style in text:
            draw_style = style
            break

    img_url = asyncio.run(draw_service.text_to_image(uid, text, dialog_id, draw_style))
    print(f"ai_draw... img_url: {img_url}")

    return Response.success(200, "获取图片成功", img_url)


@drawAI_bp.route("/<int:uid>", methods=["GET"])
def get_all_draws_chat(uid):
    """
        uid: 用户id
    """
    user_all_draws_info = draw_service.get_all_info(uid)

    # for key, values in user_all_draws_info.items():
    #     for value in values:
    #         print(f"value: {value}")

    return Response.success(200, "获取所有绘画记录成功", user_all_draws_info)
