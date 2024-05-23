import pytest
import json
from apis.ai_draw import drawAI_bp
from utils.draw_utils import query_result
from services.draw_service import text_to_image


def test_query_result():
    taskId = 18767779
    response = query_result(taskId)
    print(response)


def test_text_to_image():
    uid = 2
    text = "我想要一幅油画"
    dialog_id = 1

    response = text_to_image(uid, text, dialog_id)
    print(response)


def test_text_convert_image():
    uid = 2
    text = "我想要山水画"
    dialog_id = 1

    response = drawAI_bp.get("/draws/image", json={"uid": uid, "text": text, "dialog_id": dialog_id})
    print(response)
