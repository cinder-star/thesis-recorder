from django.urls import path
from .views import *

urlpatterns = [path("sentence", view=UploadSentences.as_view())]
