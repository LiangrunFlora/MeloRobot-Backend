import json

import requests


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=MD8Yqq2yYA0ox52Hu8WvpWPY&client_secret=12QK4F9C6TKtwT0diqKQkylcBnypNcsZ"
    # grant_type = "client_credentials"
    # base_url = "https://aip.baidubce.com/oauth/2.0/token"
    #
    # url = f"{base_url}?grant_type={grant_type}&client_id={AccessKey.API_KEY}&client_secret={AccessKey.SECRET_KEY}"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")