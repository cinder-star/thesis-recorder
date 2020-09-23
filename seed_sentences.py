import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thesis_recorder.settings")
django.setup()

from faker import Faker
from django_seed import Seed

from handle_sentence.models import Sentence

seeder = Seed.seeder()
fake = Faker()

seeder.add_entity(
    Sentence,
    10,
    {
        "sentence": lambda x: fake.sentence(),
    }
)

seeder.execute()
print("Done!")