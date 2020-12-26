from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r
from django.http import HttpResponse

import pandas as pd
from io import StringIO

from handle_sentence.models import Recording

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
