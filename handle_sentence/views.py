import random

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import permissions

from .serializers import SentenceSerializer
from .models import Sentence

# Create your views here.
class SentenceRetrieveView(ListAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = SentenceSerializer

    def get_queryset(self):
        id = self.request.query_params.get("id", None)
        if id:
            return Sentence.objects.filter(id=id)
        total = Sentence.objects.count()
        return Sentence.objects.filter(id=random.randint(1, total))
