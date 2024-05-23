import time

from DAO import draw_dao
from utils import draw_utils
from models.dialog_list import DialogList
import json
import asyncio


def new_draw_chat(uid, title):
    """
        初始化一个绘图对话
    """
    return draw_dao.insert_dialog(uid, title)


async def get_task_id(text, style):
    return await draw_utils.submit_request(text, style)


async def get_draw_content(taskId):
    return await draw_utils.query_result(taskId)


async def text_to_image(uid, text, dialog_id, style="探索无限"):
    """"
        根据文本获取图片
        并将相应信息插入数据库
        返回图片的url
    """
    # print("text: " + text)
    # print("style: " + style)
    # 发起请求
    taskId = await get_task_id(text, style)
    print(f"draw_service... taskId: {taskId}")

    time.sleep(10)

    # 查询结果
    response = await get_draw_content(taskId)
    img_url = response["data"]["img"]

    # 更新数据库
    new_image_content = draw_dao.insert_draw_content(url=img_url, uid=uid, text=text, dialog_id=dialog_id)
    dialog = DialogList.query.filter_by(id=dialog_id).first()
    message_list = dialog.message_list + f"{new_image_content.id} "
    draw_dao.update_dialog(id=dialog_id, message_list=message_list)

    draw_content = {
        "id": new_image_content.id,
        "message": "",
        "extension": new_image_content.url,
        "message_type": 1,
        "u_message": new_image_content.text,
        "uid": new_image_content.uid
    }

    return draw_content


def get_all_draw_info(uid):
    """
        获取用户的所有绘画记录
        uid: 用户id
    """
    results = draw_dao.get_all_dialog(uid=uid)
    draw_dialogs = []
    for result in results:
        result = result.to_dict()
        del result["message_list"]
        draw_dialogs.append(result)

    return draw_dialogs


def get_draw_detail(dialog_id):
    """
        获取对话的详细信息
    """
    results = draw_dao.get_all_draw_content(dialog_id=dialog_id)
    draw_contents = []
    for result in results:
        result = result.to_dict()
        draw_content = {
            "id": result["id"],
            "message": "",
            "extension": result["url"],
            "message_type": 1,
            "u_message": result["text"],
            "uid": result["uid"]
        }
        draw_contents.append(draw_content)

    return draw_contents
