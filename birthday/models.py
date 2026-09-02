from django.db import models


class Birthday(models.Model):
    class Relation(models.TextChoices):
        Friend = "FRIEND", "دوست"
        # Friend = 'FRIEND', 'دوست'

    name = models.CharField(max_length=250)
    relation = models.CharField(max_length=10, choices=Relation.choices)
    birthday_date = models.DateField()

    class Meta:
        ordering = ["-birthday_date"]
