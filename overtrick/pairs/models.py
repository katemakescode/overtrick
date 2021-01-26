from django.db import models
from almanac.models import Session


class Pair(models.Model):
    ORIENTATION_CHOICES = (
        ('NS', 'North/South'),
        ('EW', 'East/West'),
    )

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    orientation = models.CharField(max_length=2, choices=ORIENTATION_CHOICES)
    number = models.IntegerField()
    player_a = models.CharField(max_length=25)
    player_b = models.CharField(max_length=25)
    points = models.IntegerField()

    class Meta:
        ordering = ['-orientation', '-points']

    def __str__(self):
        return f'{self.orientation} #{self.number} ' \
               f'{self.player_a}/{self.player_b}'
