from random import choice

from flask.views import MethodView
from flask import request, jsonify, make_response

from src import db
from src.models import Sentence

def choose_random(string):
    all_sentences = set(x for x in range(1, 6))
    covered_sentences = set()
    if len(string) > 0:
        covered_sentences = set(map(int, string.split(", ")))
    not_covered = list(all_sentences - covered_sentences)
    new_sentence_no = choice(not_covered)
    return {
        "number": new_sentence_no,
        "sentence": Sentence.query.filter_by(id=new_sentence_no).first().sentence
    }


class SentenceAPI(MethodView):
    def post(self):
        string_list = request.form.get("all_strings")
        response_object = choose_random(string_list)
        return make_response(jsonify(response_object)), 200