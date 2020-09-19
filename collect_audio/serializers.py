from core.serializers import CoreSerializer
from .models import Dummy


class DummySerializer(CoreSerializer):
    class Meta(CoreSerializer.Meta):
        model = Dummy
