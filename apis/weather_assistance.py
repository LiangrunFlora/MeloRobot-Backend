import requests
from flask import Blueprint, jsonify

from utils.Response import Response

weather_bp = Blueprint(name="weather_assistance", import_name=__name__, url_prefix="/weather")


@weather_bp.get('/weather_details')
def get_weather_details():
    url = "https://restapi.amap.com/v3/weather/weatherInfo?city=430100&key=859de4d70a2f28468a1f453162160928"
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        print(weather_data)

        if weather_data['status'] == '1':  # 检查 API 返回状态是否成功
            lives_data = weather_data['lives'][0]
            # 进行天气信息的整合
            province = lives_data['province']
            city = lives_data['city']
            humidity = lives_data['humidity']
            report_time = lives_data['reporttime']
            temperature = lives_data['temperature']
            weather = lives_data['weather']
            wind_direction = lives_data['winddirection']
            wind_power = lives_data['windpower']
            weather_info = f"当前{report_time},{province}{city}的天气是{weather},湿度{humidity},温度{temperature},风力{wind_power},风向{wind_direction}"
            weather_info_data = {"weather_info": weather_info}
            return Response.success(data=weather_info_data)
        else:
            return Response.error()
    except requests.RequestException as e:
        return Response.error()


