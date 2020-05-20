from flask import Blueprint

from src.views.auth.Register import RegisterAPI
from src.views.auth.Login import LoginAPI
from src.views.auth.User import UserAPI
from src.views.auth.Logout import LogoutAPI
from src.views.staticfiles.Home import HomeAPI
from src.views.staticfiles.Js import JsAPI

auth_blueprint = Blueprint("auth", __name__)

# define the API resources
registration_view = RegisterAPI.as_view("register_api")
login_view = LoginAPI.as_view("login_api")
user_view = UserAPI.as_view("user_api")
logout_view = LogoutAPI.as_view("logout_api")
home_view = HomeAPI.as_view("home_api")
js_view = JsAPI.as_view("js_api")

# add Rules for API Endpoints
auth_blueprint.add_url_rule("/", view_func=home_view, methods=["GET"])
auth_blueprint.add_url_rule(
    "/auth/register", view_func=registration_view, methods=["POST"]
)
auth_blueprint.add_url_rule("/auth/login", view_func=login_view, methods=["POST"])
auth_blueprint.add_url_rule("/auth/status", view_func=user_view, methods=["GET"])
auth_blueprint.add_url_rule("/auth/logout", view_func=logout_view, methods=["POST"])
auth_blueprint.add_url_rule("/js/<path:filename>", view_func=js_view, methods=["GET"])