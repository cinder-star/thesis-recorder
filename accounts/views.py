from django.http import HttpResponseRedirect
from accounts.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    UserSerializer,
    UserSerializerWithToken,
    TokenObtainCustomSerializer,
)


@api_view(["GET"])
def current_user(request):

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainCustomSerializer
