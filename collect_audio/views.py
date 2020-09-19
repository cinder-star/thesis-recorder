from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import authentication_classes, permission_classes

from .serializers import DummySerializer
from .models import Dummy

# Create your views here.


class HelloView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication,
        authentication.BasicAuthentication,
    ]

    def get(self, response):
        content = {"message": "Hello world"}
        return Response(content)


class DummyView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = DummySerializer
    queryset = Dummy.objects.all()
