from django.urls import path
from . import views

urlpatterns = [
    path("normal/", views.NormalView.as_view()),
    path("new_sentence/", views.NewSentenceView.as_view()),
]
