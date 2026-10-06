from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0002_import_decanat_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="exchangeprogram",
            name="country",
            field=models.CharField(default="", max_length=100, verbose_name="Країна"),
            preserve_default=False,
        ),
    ]
