from handle_sentence.models import Sentence
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

# Create your views here.


class UploadSentences(APIView):
    def post(self, request, *args, **kwargs):
        try:
            file = request.FILES["file"]
            df = pd.read_csv(file)
            Sentence.objects.bulk_create(
                [
                    Sentence(sentence=single_sentence)
                    for single_sentence in df["sentence"]
                ]
            )
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e.__str__())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
