from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class UserSerializerWithToken(serializers.ModelSerializer):

    access = serializers.SerializerMethodField()
    refresh = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_access(self, user):
        token = AccessToken().for_user(user).__str__()
        return token

    def get_refresh(self, user):
        token = RefreshToken().for_user(user).__str__()
        return token

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ("access", "refresh", "username", "password")
