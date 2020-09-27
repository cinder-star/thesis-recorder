from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("current_user/", views.current_user),
    path("register/", views.UserList.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh_token/", TokenRefreshView.as_view()),
]
