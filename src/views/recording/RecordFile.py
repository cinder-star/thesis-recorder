from flask.views import MethodView
from flask import request, jsonify, make_response

from src import db, storage_bucket
from src.models import Sentence, Recording
from src.views.recording.Sentence import SentenceAPI

class RecordAPI(SentenceAPI):
    def post(self):
        file = request.files["audio"]
        filename = request.form.get("filename")
        blob = storage_bucket.blob(filename)
        blob.upload_from_file(file)
        return super().post()