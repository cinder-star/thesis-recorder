from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    gender = models.CharField(max_length=10, null=True, blank=True, default=None)
    age = models.IntegerField(null=True, blank=True, default=0)
