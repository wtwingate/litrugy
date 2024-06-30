# Generated by Django 5.0.6 on 2024-06-30 02:15

import json
from django.db import migrations


def seed_lesson(apps, _):
    Lesson = apps.get_model("lectionary", "Lesson")
    with open("data/lectionary.json") as f:
        data = json.load(f)

    for day_name, v in data.items():
        if day_name == "Christmas Day" or day_name == "Easter Day":
            for years in v.values():
                for lessons in years.values():
                    for lesson_list in lessons.values():
                        scripture = " or ".join(lesson_list)
                        lesson_object, _ = Lesson.objects.get_or_create(
                            scripture=scripture
                        )
                        lesson_object.save()
        else:
            for lessons in v.values():
                for lesson_list in lessons.values():
                    scripture = " or ".join(lesson_list)
                    lesson_object, _ = Lesson.objects.get_or_create(scripture=scripture)
                    lesson_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ("lectionary", "0002_seed_day"),
    ]

    operations = [migrations.RunPython(seed_lesson)]
