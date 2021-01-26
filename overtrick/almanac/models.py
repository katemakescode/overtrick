from django.db import models


class Session(models.Model):
    TIME_CHOICES = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('E', 'Evening'),
    )

    club = models.CharField(max_length=20)
    date = models.DateField()
    time = models.CharField(max_length=1, choices=TIME_CHOICES)
    event = models.CharField(max_length=40)

    class Meta:
        ordering = ['-date', 'time']

    def __str__(self):
        return f'{self.club}: {self.date} {self.time}'
