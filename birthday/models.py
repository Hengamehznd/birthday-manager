from datetime import date

from django.db import models


class Birthday(models.Model):
    class Relation(models.TextChoices):
        FRIEND = "FRIEND", "دوست"
        FAMILY = "FAMILY", "خانواده"
        COLLEAGUE = "COLLEAGUE", "همکار"
        OTHER = "OTHER", "سایر"
    name = models.CharField(max_length=250, verbose_name="نام و نام خانوادگی")
    relation = models.CharField(
        max_length=10,
        choices=Relation.choices,
        verbose_name="نسبت",
    )
    birthday_date = models.DateField(verbose_name="تاریخ تولد")

    class Meta:
        ordering = ["birthday_date"]
        verbose_name = "تولد"
        verbose_name_plural = "تولدها"

    def __str__(self):
        return self.name

    @property
    def age(self):
        today = date.today()
        return today.year - self.birthday_date.year - (
            (today.month, today.day)
            < (self.birthday_date.month, self.birthday_date.day)
        )

    @property
    def days_until_birthday(self):
        today = date.today()
        next_birthday = self.birthday_date.replace(year=today.year)

        if next_birthday < today:
            next_birthday = self.birthday_date.replace(year=today.year + 1)

        return (next_birthday - today).days
