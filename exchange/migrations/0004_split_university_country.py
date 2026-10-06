import re

from django.db import migrations

IN_PARENTHESES = re.compile(r"^(?P<name>.+?)\s*\((?P<country>[^()]+)\)$")
AFTER_SEPARATOR = re.compile(r"^(?P<name>.+?)\s*(?:,|\s[-–—]\s)\s*(?P<country>[^,]+)$")


def parse_university(raw):
    value = raw.strip()
    for pattern in (IN_PARENTHESES, AFTER_SEPARATOR):
        match = pattern.match(value)
        if match:
            return match.group("name").strip(), match.group("country").strip()
    raise ValueError(f"Не вдалося розділити університет і країну: {raw!r}")


def split_university_country(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.university, program.country = parse_university(program.university)
        program.save(update_fields=["university", "country"])


def join_university_country(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.university = f"{program.university}, {program.country}"
        program.save(update_fields=["university"])


class Migration(migrations.Migration):
    dependencies = [
        ("exchange", "0003_add_country"),
    ]

    operations = [
        migrations.RunPython(split_university_country, join_university_country),
    ]
