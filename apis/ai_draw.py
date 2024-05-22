import json

from flask import request
from flask import Blueprint
from utils.Response import Response
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

    draw_content = asyncio.run(draw_service.text_to_image(uid, text, dialog_id, draw_style))

    return Response.success(200, "获取图片成功", draw_content)


@drawAI_bp.route("/<int:uid>", methods=["GET"])
def get_all_draws_chat(uid):
    """
        获取用户的所有绘画记录
        uid: 用户id
        id title uid
    """
    draw_dialogs = draw_service.get_all_draw_info(uid)
    print(draw_dialogs)

    return Response.success(200, "获取所有绘画记录成功", draw_dialogs)


@drawAI_bp.route("/<int:dialog_id>/detail", methods=["GET"])
def get_draw_detail(dialog_id):
    """
        获取绘画对话的详细信息
        dialog_id: 对话id
    """
    draw_detail = draw_service.get_draw_detail(dialog_id)
    print(draw_detail)

    return Response.success(200, "获取绘画对话详细信息成功", draw_detail)
