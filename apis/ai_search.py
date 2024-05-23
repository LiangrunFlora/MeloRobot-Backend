import json

import requests
from flask import Blueprint, request

from services.ai_search.search_util import get_access_token
from utils.Response import Response
from utils.SearchInfo import SearchInfo

searchAI_bp = Blueprint(name="ai_search", import_name=__name__, url_prefix="/ai_search")


# 获取搜索响应数据
@searchAI_bp.get('/search/<string:searchMsg>')
def get_search_response(searchMsg):
    # query = request.args.get('q')
    # if not query:
    #     return Response.error()

    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': 'AIzaSyBi_cmvD4k5Uis-kaiKqDXkIh4i7ad4nOI',
        'cx': '8451c643cf7cf45a4:omuauf_lfve',
        'q': searchMsg
    }

    response = requests.get(url, params=params)
    return Response.success(data=response.json())


# 总结响应数据并返回
@searchAI_bp.get('/summary/<string:searchMsg>')
def get_ai_summary(searchMsg):
    print(searchMsg)
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-4.0-8k-preview?access_token=" + get_access_token()

    searchMsg += "给我提取这些信息的关键点，以问题和回答的形式写出3个问题，共500字的总结"
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": searchMsg
            }
        ]
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    # 将响应体内容转化为字典
    chat_data = response.json()
    # # 打印回复内容
    # chat_data = [chat_data]
    print(chat_data)
    msg = "获取回复成功"
    return Response.success(data=chat_data)


