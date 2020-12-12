import random

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from .serializers import SentenceSerializer
from .models import Sentence
from .utils import get_sentece_by_id

# Create your views here.
class SentenceRetrieveView(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    def get(self, *args, **kwargs):
        id = self.request.query_params.get("id", None)
        data = get_sentece_by_id(id)
        return Response(data=data, status=status.HTTP_200_OK)
