from django.db import models


class FacultyInfo(models.Model):
    name = models.CharField("Назва факультету", max_length=160)
    description = models.TextField("Опис")
    contacts = models.TextField("Контакти")

    class Meta:
        verbose_name = "Інформація про факультет"
        verbose_name_plural = "Інформація про факультет"

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField("Назва", max_length=150)
    head = models.CharField("Завідувач кафедри", max_length=120)

    class Meta:
        ordering = ["id"]
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедри"

    def __str__(self):
        return self.name


class Program(models.Model):
    LEVEL_CHOICES = [
        ("bachelor", "Бакалаврський"),
        ("master", "Магістерський"),
    ]

    name = models.CharField("Назва", max_length=200)
    code = models.CharField("Код", max_length=20)
    level = models.CharField(
        "Рівень", max_length=10, choices=LEVEL_CHOICES, default="bachelor"
    )
    description = models.TextField("Опис")
    coordinator_name = models.CharField("Ім'я координатора набору", max_length=120)
    coordinator_contact = models.CharField(
        "Контакт координатора набору", max_length=160
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="programs",
        verbose_name="Випускова кафедра",
    )
    disciplines = models.TextField("Дисципліни", blank=True)

    class Meta:
        ordering = ["level", "id"]
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"

    def __str__(self):
        return f"{self.code} - {self.name} ({self.get_level_display()})"

    def disciplines_list(self):
        return [line.strip() for line in self.disciplines.splitlines() if line.strip()]


class Teacher(models.Model):
    name = models.CharField("Ім'я", max_length=120)
    position = models.CharField("Посада", max_length=100)
    degree = models.CharField("Науковий ступінь", max_length=100, blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="teachers",
        verbose_name="Кафедра",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"

    def __str__(self):
        return self.name
