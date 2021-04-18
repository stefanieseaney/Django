import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django

django.setup()

from learning_logs.models import Topic, Entry

topics = Topic.objects.all()
entries = Entry.objects.all()

t = Topic.objects.get(id=1)
print(t)

entry = t.entry_set.all()
print(entry)

for t in topics:
    print(f"Topic ID: {t.id} and Topic Name: {t}")
    print(f"Date added: {t.date_added}")

for e in entries:
    print(f"Topic: {e.topic}")
    print(f"Entry: {e.text}")
