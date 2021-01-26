from django.db import models
from django.utils.translation import gettext_lazy as _


class Session(models.Model):
    class Time(models.TextChoices):
        MORNING = 'M', _('Morning')
        AFTERNOON = 'A', _('Afternoon')
        EVENING = 'E', _('Evening')

    club = models.CharField(max_length=20)
    date = models.DateField()
    time = models.CharField(
        max_length=1,
        choices=Time.choices,
        default=Time.EVENING,
    )
    event = models.CharField(max_length=40)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['club', 'date', 'time', 'event'],
                name='unique session'
            )
        ]
        ordering = ['-date', 'time']

    def __str__(self):
        return f'{self.club}: {self.date} {self.time} {self.event}'
