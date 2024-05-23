# 当识别到天气的时候调用
from flask import jsonify

from apis.weather_assistance import get_weather_details


def get_weather_util():
    response = get_weather_details()
    res_data = response['data']
    lives_data = res_data['lives']
    #进行天气信息的整合
    province = lives_data['province']
    city = lives_data['city']
    humidity = lives_data['humidity']
    report_time = lives_data['reporttime']
    temperature = lives_data['temperature']
    weather = lives_data['weather']
    wind_direction = lives_data['winddirection']
    wind_power = lives_data['windpower']
    weather_info = f"当前{report_time},{province}{city}的天气是{weather},湿度{humidity},温度{temperature},风力{wind_power},风向{wind_direction}"
    weather_data = {"weather_info": weather_info}
    print(jsonify(weather_data))
    return jsonify(weather_data)







