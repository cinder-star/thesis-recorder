from flask import send_from_directory
from flask.views import MethodView

class HomeAPI(MethodView):
    def get(self):
        return send_from_directory("static/templates", "index.html")