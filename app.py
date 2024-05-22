import json

from flask import Flask, request
from extensions import db
from flask_cors import CORS
import config
from flask_migrate import Migrate
from services import draw_service
from utils.Response import Response
from utils.draw_utils import styles

# from models.chat import Chat
# from models.dialog_list import DialogList
# from models.draw_content import DrawContent
# from models.interaction import Interaction
# from models.users import User


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)
CORS(app, resources=r'/*')


@app.route("/draws", methods=["POST"])
def initial_chat():
    """
        uid: 本次聊天用户的id
        title: 本次聊天的标题
    """
    uid = request.json.get("uid")
    title = request.json.get("title")

    draw_service.new_draw_chat(uid, title)
    return Response.success(200, "初始化绘画对话成功")


@app.route("/draws/image", methods=["POST"])
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

    img_url = draw_service.text_to_image(uid, text, dialog_id, draw_style)
    return Response.success(200, "获取图片成功", img_url)


@app.route("/draws/<int:uid>", methods=["GET"])
def get_all_draws_chat(uid):
    """
        uid: 用户id
    """
    user_all_draws_info = draw_service.get_all_info(uid)

    # for key, values in user_all_draws_info.items():
    #     for value in values:
    #         print(f"value: {value}")

    return Response.success(200, "获取所有绘画记录成功", user_all_draws_info)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
