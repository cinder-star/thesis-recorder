import os

from django.core.files.storage import FileSystemStorage

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from handle_sentence.models import Sentence, Recording
from handle_sentence.utils import get_sentece_by_id


class NormalView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def post(self, request, format=None):
        filename = request.data["filename"]
        file = request.FILES["audio"]
        try:
            next_id = int(request.data["next_id"])
        except ValueError:
            next_id = None
        fs = FileSystemStorage()
        fs.save(filename, file)
        sentence_id = filename.split("-")[0]
        sentence = Sentence.objects.get(id=sentence_id)
        sentence.total_records += 1
        sentence.save()

        user = self.request.user
        if not user.is_authenticated:
            user = None
        file_size = os.path.getsize(os.path.join("media", filename))
        Recording.objects.create(
            sentence=sentence, filename=filename, size=file_size, user=user,
        )

        data = get_sentece_by_id(next_id)
        return Response(data=data, status=status.HTTP_200_OK)


class NewSentenceView(NormalView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        sentence = request.data["sentence"]
        if len(sentence) == 0:
            return Response(
                data={"details": "Empty sentence"},
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )
        try:
            db_instance = Sentence.objects.get(sentence=sentence)
            request.data["filename"] = "".join(
                [str(db_instance.id), "-", request.data["filename"]]
            )
        except:
            new_sentence = Sentence.objects.create(sentence=sentence)
            request.data["filename"] = "".join(
                [str(new_sentence.id), "-", request.data["filename"]]
            )
        return super().post(request, format)
