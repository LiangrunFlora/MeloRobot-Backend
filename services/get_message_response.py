import json
import requests


def get_message_response(message: str):
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

    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode('utf-8'))
            collected_response += data['response']
            # print(f"Received chunk: {data['response']}")  # 打印每个流式响应结果

    # 将聊天信息添加到数据库中


    return collected_response


def get_image_response(message:str, image_base64: str):
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

    # 将聊天信息添加到数据库中
    return collected_response


if __name__ == '__main__':
    print(get_image_response("hello", "123"))
