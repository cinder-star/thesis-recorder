from rest_framework import serializers
from accounts.models import User
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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
        fields = ("access", "refresh", "username", "password", "is_superuser")


class TokenObtainCustomSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        raw_data = super().validate(attrs)
        raw_data["is_superadmin"] = self.user.is_staff
        return raw_data
