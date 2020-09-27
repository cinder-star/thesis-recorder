from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Sentence


class SentenceSerializer(ModelSerializer):
    total_sentences = SerializerMethodField(read_only=True)

    def get_total_sentences(self, instance):
        return Sentence.objects.count()

    class Meta:
        fields = ["id", "sentence", "total_sentences"]
        model = Sentence
