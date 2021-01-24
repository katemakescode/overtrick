from django.db import models


class Session(models.Model):
    club = models.CharField(max_length=20)
    date = models.DateField()
    time = models.CharField(max_length=10)
    event = models.ForeignKey
