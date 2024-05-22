from flask import Blueprint,request
from services.get_message_response import get_message_response, get_image_response
from services.user import login_valid, add_user
from utils.Response import Response

user_bp = Blueprint(name="user", import_name=__name__, url_prefix="/")


@user_bp.post("login")
def login():
    data = request.json
    account = data.get("account")
    password = data.get("password")
    if account and password:
        user = login_valid(account, password)
        if user:
            return Response.success(data=user)
    else:
        return Response.error(message="账户不存在或密码错误")


@user_bp.post("register")
def register():
    data = request.json
    account = data['account']
    password = data['password']
    email = data['email']
    new_user = add_user(account, password, email)
    if new_user:
        return Response.success(data=new_user)
    else:
        return Response.error(message="当前邮箱已注册")
