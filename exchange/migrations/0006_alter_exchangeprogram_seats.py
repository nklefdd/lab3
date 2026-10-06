from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0005_normalize_seats"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exchangeprogram",
            name="seats",
            field=models.PositiveIntegerField(verbose_name="Кількість місць"),
        ),
    ]
