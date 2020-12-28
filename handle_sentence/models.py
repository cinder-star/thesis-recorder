from django.db import models
from core.models import CoreModel
from django.contrib.auth.models import User

# Create your models here.
class Sentence(CoreModel):
    sentence = models.CharField(max_length=200, null=False, blank=False)
    total_records = models.IntegerField(default=0, null=True, blank=True)
    verified_records = models.IntegerField(default=0, null=True, blank=True)


class Recording(CoreModel):
    sentence = models.ForeignKey(
        Sentence, blank=True, null=True, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, blank=True, null=True, default=None, on_delete=models.SET_NULL
    )
    filename = models.CharField(max_length=100, null=True, blank=True)
    size = models.IntegerField(default=0, blank=True, null=True)
