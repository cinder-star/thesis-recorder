from flask import send_from_directory
from flask.views import MethodView

class JsAPI(MethodView):
    def get(self, filename):
        return send_from_directory("static/js", filename)