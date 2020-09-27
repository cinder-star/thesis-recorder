from django.core.files.storage import FileSystemStorage

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from handle_sentence.models import Sentence

class NormalView(APIView):
    permission_classes = [AllowAny,]
    def post(self, request, format=None):
        try:
            filename = request.data["filename"]
            file = request.FILES["audio"]
            fs = FileSystemStorage()
            fs.save(filename, file)
            sentence_id = filename.split("-")[0]
            sentence = Sentence.objects.get(id=sentence_id)
            sentence.total_records += 1
            sentence.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NewSentenceView(NormalView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        sentence = request.data["sentence"]
        try:
            db_instance = Sentence.objects.get(sentence=sentence)
            request.data["filename"] = "".join([str(db_instance.id),"-",request.data["filename"]])
        except:
            new_sentence = Sentence.objects.create(sentence=sentence)
            request.data["filename"] = "".join([str(new_sentence.id),"-",request.data["filename"]])
        return super().post(request, format)