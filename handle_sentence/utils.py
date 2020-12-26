from .models import Sentence
import random


def get_sentece_by_id(id=None):
    total = Sentence.objects.count()
    final_id = None
    sentence = None
    if id:
        final_id = int(id)
        sentence = Sentence.objects.get(id=id).sentence
    else:
        final_id = random.randint(1, total)
        sentence = Sentence.objects.get(id=final_id).sentence
    data = {
        "total_senteces": total,
        "id": final_id,
        "sentence": sentence,
    }
    return data
