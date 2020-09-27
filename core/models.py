from django.db import models
from django.utils import timezone

# Create your models here.
class CoreModel(models.Model):
    id = models.AutoField(null=False, editable=False, primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
