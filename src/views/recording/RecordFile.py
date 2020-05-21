import asyncio

from flask.views import MethodView
from flask import request, jsonify, make_response

from src import db, storage_bucket
from src.models import Sentence, Recording
from src.views.recording.Sentence import SentenceAPI

async def firebase_post(file, filename):
    blob = storage_bucket.blob(filename)
    blob.upload_from_file(file)

class RecordAPI(MethodView):
    def post(self):
        response_object = {}
        try:
            file = request.files["audio"]
            filename = request.form.get("filename")
            sentece_no = filename.split("-")[0]
            sentence = Sentence.query.filter_by(id=int(sentece_no)).first()
            sentence.samples += 1
            recording = Recording(filename, int(sentece_no))
            db.session.add(recording)
            db.session.commit()
            firebase_post(file, filename)
        except Exception as e:
            raise e
        return make_response(jsonify(response_object)), 200