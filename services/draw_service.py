from DAO import draw_dao
from utils import draw_utils
from models.dialog_list import DialogList
import json


def new_draw_chat(uid, title):
    """
        初始化一个绘图对话
    """
    return draw_dao.insert_dialog(uid, title)


def text_to_image(uid, text, dialog_id, style="探索无限"):
    """"
        根据文本获取图片
        并将相应信息插入数据库
        返回图片的url
    """
    # print("text: " + text)
    # print("style: " + style)
    # 发起请求
    submit_response = draw_utils.submit_request(text, style)
    taskId = submit_response.json()["data"]["taskId"]
    # print("taskId: " + taskId)
    # 查询结果
    img_url = draw_utils.query_result(taskId)

    # 更新数据库
    new_image_content = draw_dao.insert_draw_content(url=img_url, uid=uid, text=text, dialog_id=dialog_id)
    dialog = DialogList.query.filter_by(id=dialog_id).first()
    message_list = dialog.message_list + f"{new_image_content.id} "
    draw_dao.update_dialog(id=dialog_id, message_list=message_list)

    return img_url


def get_all_info(uid):
    """
        在用户重新登录时，获取所有信息
        返回一个字典变量:
            {
                dialog_id : [draw_content...]
            }
    """
    results = {}

    dialogs = draw_dao.get_all_dialog(uid=uid)

    for dialog in dialogs:
        print(f"dialog: {dialog.id}")
        results[dialog.id] = draw_dao.get_all_draw_content(dialog_id=dialog.id)

    return results
