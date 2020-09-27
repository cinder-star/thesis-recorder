from rest_framework.serializers import ModelSerializer
from .models import CoreModel


class CoreSerializer(ModelSerializer):
    class Meta:
        model = CoreModel
        exclude = tuple(
            f.name
            for f in CoreModel._meta.get_fields()
            if not (f.name == "created_at" or f.name == "id")
        )
        print(exclude)
        abstract = True
