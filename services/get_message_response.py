import json
import requests

from DAO.chat import insert_interaction_message
from flask import jsonify, Response, stream_with_context


def get_message_response(message: str, uid: int):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers, stream=True)

    collected_response = ""

    # for line in response.iter_lines():
    #     if line:
    #         data = json.loads(line.decode('utf-8'))
    #         collected_response += data['response']
    #         # print(f"Received chunk: {data['response']}")  # 打印每个流式响应结果
    def generate_response():
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                yield f"{data['response']}"

    return Response(stream_with_context(generate_response()), content_type='text/plain')
    # 将聊天信息添加到数据库中
    # interaction_message = insert_interaction_message(message=collected_response, message_type=0, u_message=message,
    #                                                  uid=uid)
    # return interaction_message.to_dict()


def get_image_response(message: str, image_base64: str, uid: int):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llava",
        "prompt": message,
    }
    if image_base64.startswith("data:/image/"):
        image_base64_without_head = image_base64.split(",")[1]
        payload["image"] = image_base64_without_head
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers, stream=True)

    collected_response = ""

    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode('utf-8'))
            collected_response += data['response']
            print(f"Received chunk: {data['response']}")  # 打印每个流式响应结果

    # TODO: 将图片上传到图床后，返回URL
    image_url = ""

    # 将聊天信息添加到数据库中
    interaction_message = insert_interaction_message(message=collected_response,
                                                     message_type=1,
                                                     u_message=message,
                                                     uid=uid,
                                                     extension=image_url)
    return interaction_message.to_dict()


if __name__ == '__main__':
    print(get_message_response("hello", 1))
