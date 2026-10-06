import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150, verbose_name="Назва")),
                ("head", models.CharField(max_length=120, verbose_name="Завідувач кафедри")),
            ],
            options={
                "verbose_name": "Кафедра",
                "verbose_name_plural": "Кафедри",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="FacultyInfo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=160, verbose_name="Назва факультету")),
                ("description", models.TextField(verbose_name="Опис")),
                ("contacts", models.TextField(verbose_name="Контакти")),
            ],
            options={
                "verbose_name": "Інформація про факультет",
                "verbose_name_plural": "Інформація про факультет",
            },
        ),
        migrations.CreateModel(
            name="Program",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200, verbose_name="Назва")),
                ("code", models.CharField(max_length=20, verbose_name="Код")),
                ("level", models.CharField(choices=[("bachelor", "Бакалаврський"), ("master", "Магістерський")], default="bachelor", max_length=10, verbose_name="Рівень")),
                ("description", models.TextField(verbose_name="Опис")),
                ("coordinator_name", models.CharField(max_length=120, verbose_name="Ім'я координатора набору")),
                ("coordinator_contact", models.CharField(max_length=160, verbose_name="Контакт координатора набору")),
                ("disciplines", models.TextField(blank=True, verbose_name="Дисципліни")),
                ("department", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="programs", to="faculty.department", verbose_name="Випускова кафедра")),
            ],
            options={
                "verbose_name": "Спеціальність",
                "verbose_name_plural": "Спеціальності",
                "ordering": ["level", "id"],
            },
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120, verbose_name="Ім'я")),
                ("position", models.CharField(max_length=100, verbose_name="Посада")),
                ("degree", models.CharField(blank=True, max_length=100, verbose_name="Науковий ступінь")),
                ("department", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="teachers", to="faculty.department", verbose_name="Кафедра")),
            ],
            options={
                "verbose_name": "Викладач",
                "verbose_name_plural": "Викладачі",
                "ordering": ["name"],
            },
        ),
    ]
