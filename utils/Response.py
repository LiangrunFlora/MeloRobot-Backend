from flask import jsonify


class Response:
    @staticmethod
    def success(code=200, message="请求成功", data=None):
        response = {
            "code": code,
            "message": message,
            "data": data
        }
        return jsonify(response)

    @staticmethod
    def error(code=400, message="请求失败", errors=None):
        response = {
            "status": code,
            "message": message,
            "errors": errors
        }
        return jsonify(response)
