from django.db import models


class Pair(models.Model):
    orientation = models.CharField(max_length=2)
    number = models.IntegerField()
    player_a = models.CharField(max_length=25)
    player_b = models.CharField(max_length=25)
    points = models.IntegerField()

    class Meta:
        ordering = ['-orientation', '-points']

    def __str__(self):
        return f'{self.orientation} #{self.number} ' \
               f'{self.player_a}/{self.player_b}'
