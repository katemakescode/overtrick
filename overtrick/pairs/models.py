from django.db import models
from django.utils.translation import gettext_lazy as _

from almanac.models import Session


class Pair(models.Model):
    class Orientation(models.TextChoices):
        NORTH = 'NS', _('North/South')
        EAST = 'EW', _('East/West')

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    orientation = models.CharField(
        max_length=2,
        choices=Orientation.choices,
        default=Orientation.NORTH,
    )
    number = models.IntegerField()
    player_a = models.CharField(max_length=25)
    player_b = models.CharField(max_length=25)
    points = models.IntegerField()

    @property
    def player_names(self):
        return f'{self.player_a} and {self.player_b}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['session', 'orientation', 'number'],
                name='unique pair'
            )
        ]
        ordering = ['-orientation', '-points']

    def __str__(self):
        return f'{self.orientation} #{self.number} ' \
               f'{self.player_a}/{self.player_b}'
