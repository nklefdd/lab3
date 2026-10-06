from django.db import models
from django.utils import timezone


class ExchangeProgram(models.Model):
    university = models.CharField("Університет", max_length=200)
    country = models.CharField("Країна", max_length=100)
    languages = models.CharField("Мови навчання", max_length=200)
    seats = models.PositiveIntegerField("Кількість місць")
    deadline = models.DateField("Дедлайн подачі")
    description = models.TextField("Опис")

    class Meta:
        ordering = ["deadline"]
        verbose_name = "Програма обміну"
        verbose_name_plural = "Програми обміну"

    def __str__(self):
        return f"{self.university} ({self.country})"

    @property
    def is_open(self):
        return self.deadline >= timezone.localdate()
