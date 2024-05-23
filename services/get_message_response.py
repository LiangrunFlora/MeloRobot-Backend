import json
from typing import List, Any

import requests

from DAO.chat import insert_interaction_message, get_all_interaction_dao, update_chat_list
from flask import jsonify, Response, stream_with_context

from extensions import db
from models.chat import Chat
from models.interaction import Interaction


def get_message_response(message: str, uid: int, detail_id: int):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers, stream=True)


    # for line in response.iter_lines():
    #     if line:
    #         data = json.loads(line.decode('utf-8'))
    #         collected_response += data['response']
    #         # print(f"Received chunk: {data['response']}")  # 打印每个流式响应结果
    def generate_response():
        collected_response = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                collected_response += data['response']
                yield f"{data['response']}"

        interaction_message = insert_interaction_message(message=collected_response, message_type=0, u_message=message,
                                                         uid=uid)
        update_chat_list(interaction_message, detail_id)
        return interaction_message.to_dict()
    return Response(stream_with_context(generate_response()), content_type='text/plain')



def get_image_response(message: str, image_base64: str, uid: int, detail_id: int):
    url = "http://localhost:11434/api/generate"
    images_list = []
    payload = {
        "model": "llava",
        "prompt": message,
    }
    if image_base64.startswith("data:image/"):
        image_base64_without_head = image_base64.split(",")[1]
        images_list.append(image_base64_without_head)
        payload["images"] = images_list
    headers = {
        "Content-Type": "application/json"
    }
    print(payload)

    response = requests.post(url, json=payload, headers=headers, stream=True)

    def generate_response():
        collected_response = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                collected_response += data['response']
                yield f"{data['response']}"

        interaction_message = insert_interaction_message(message=collected_response, message_type=1, u_message=message,
                                                         uid=uid, extension=image_base64)
        update_chat_list(interaction_message, detail_id)
        return interaction_message.to_dict()

    return Response(stream_with_context(generate_response()), content_type='text/plain')

    # # TODO: 将图片上传到图床后，返回URL
    # image_url = ""
    #
    # # 将聊天信息添加到数据库中
    # interaction_message = insert_interaction_message(message=collected_response,
    #                                                  message_type=1,
    #                                                  u_message=message,
    #                                                  uid=uid,
    #                                                  extension=image_url)
    # return interaction_message.to_dict()


def get_all_interaction(id: int):
    interaction_list: list[Interaction] = get_all_interaction_dao(id)
    return interaction_list


def add_new_chat(uid: int, title: str):
    chat = Chat(interaction_list="", uid=uid, title=title)
    db.session.add(chat)
    db.session.commit()
    return chat.to_dict()
