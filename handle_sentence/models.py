from django.db import models
from core.models import CoreModel

# Create your models here.
class Sentence(CoreModel):
    sentence = models.CharField(max_length=200, null=False, blank=False)
    total_records = models.IntegerField(default=0, null=True, blank=True)
    verified_records = models.IntegerField(default=0, null=True, blank=True)
