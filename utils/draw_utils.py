import requests
import json
import aiohttp


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    API_KEY = 'd5nrvgNkbgaOB1w9K138U9Ik'
    SECRET_KEY = 'sj3zg604YpnpwXJ2d04qYau15emBz21g'

    url = f"https://aip.baidubce.com/oauth/2.0/token?client_id={API_KEY}&client_secret={SECRET_KEY}&grant_type=client_credentials"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)

    return response.json()["access_token"]


async def submit_request(text, style):
    url = "https://aip.baidubce.com/rpc/2.0/ernievilg/v1/txt2img?access_token=" + get_access_token()

    payload = {
        "text": text,
        "resolution": "1024*1024",
        "style": style,
        "num": 1
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # response = requests.request("POST", url, headers=headers, json=payload)
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, headers=headers, json=payload) as response:
            data = await response.json()
            print(f"submit_request... data: {data}")
            taskId = data["data"]["taskId"]

    print(f"submit_request... taskId: {taskId}")

    """
        返回示例
        {
            "data": {
                "taskId": 18546968
            },
            "log_id": 1770407384814199933
        }
    """
    return taskId


async def query_result(taskId):
    url = "https://aip.baidubce.com/rpc/2.0/ernievilg/v1/getImg?access_token=" + get_access_token()

    payload = {
        "taskId": taskId
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # response = requests.post(url, headers=headers, json=payload)
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, headers=headers, json=payload) as response:
            data = await response.json()
            print(f"query_result... data: {data}")

    print(f"query_result... img_url: {data['data']['img']}")

    """
    {
        "data": {
            "style": "油画",
            "taskId": 18546968,
            "imgUrls": [
                {
                    "image": "",
                    "img_approve_conclusion": "paas"
                }
            ],
            "text": "睡莲",
            "status": 1,
            "createTime": "2024-03-20 19:09:49",
            "img": "ssssss",
            "waiting": "0"
        },
        "log_id": 1770407455383181085
    }
    """
    return data


styles = [
    "探索无限", "古风", "二次元", "写实风格", "浮世绘", "low poly",
    "未来主义", "像素风格", "概念艺术", "赛博朋克", "洛丽塔风格", "巴洛克风格",
    "超现实主义", "水彩画", "蒸汽波艺术", "油画", "卡通画"
]
