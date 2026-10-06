import re

from django.db import migrations


def normalize_seats(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        match = re.search(r"\d+", program.seats)
        if match is None:
            raise ValueError(f"У кількості місць немає числа: {program.seats!r}")
        program.seats = match.group()
        program.save(update_fields=["seats"])


class Migration(migrations.Migration):
    dependencies = [
        ("exchange", "0004_split_university_country"),
    ]

    operations = [
        migrations.RunPython(normalize_seats, migrations.RunPython.noop),
    ]
