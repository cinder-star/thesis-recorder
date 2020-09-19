from django.db import models

from core.models import CoreModel

# Create your models here.


class Dummy(CoreModel):
    name = models.CharField(max_length=20, null=False, blank=False)
