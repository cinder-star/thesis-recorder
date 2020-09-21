from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import views

urlpatterns = [
    path("current_user/", views.current_user),
    path("register/", views.UserList.as_view()),
    path("login/", obtain_jwt_token),
    path("refresh_token/", refresh_jwt_token),
]
