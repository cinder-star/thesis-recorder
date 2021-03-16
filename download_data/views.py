import os
from io import BytesIO
from os.path import basename
from download_data.utils import get_recording_list
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r
from django.http import HttpResponse

import pandas as pd
import zipfile

from handle_sentence.models import Recording
from thesis_recorder.settings import MEDIA_ROOT

# Create your views here.


class RecordingData(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, *args, **kwargs):
        recording_data_list = list(
            Recording.objects.all().values_list(
                "filename", "size", "sentence__sentence"
            )
        )

        df = pd.DataFrame(recording_data_list, columns=["filename", "size", "sentence"])
        csv = df.to_csv()

        response = HttpResponse(csv, content_type="application/csv")
        response["Content-Disposition"] = 'attachment; filename="train.csv"'
        return response


class RecordingFiles(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, *args, **kwargs):
        id = self.request.query_params.get("id", None)
        recording_list = get_recording_list(id)
        zipfilename = "recordings.zip"
        if id:
            zipfilename = "".join([f"{id}", "-", zipfilename])
        response = HttpResponse(content_type="application/zip")
        with zipfile.ZipFile(response, "w") as zipme:
            for file in recording_list:
                filepath = os.path.join(MEDIA_ROOT, file)
                zipme.write(filepath, file, compress_type=zipfile.ZIP_DEFLATED)

        response["Content-Disposition"] = f'attachment; filename="{zipfilename}"'
        return response
