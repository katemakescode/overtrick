# Generated by Django 3.1.5 on 2021-01-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almanac', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ['-date', 'time']},
        ),
        migrations.AlterField(
            model_name='session',
            name='time',
            field=models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('E', 'Evening')], max_length=1),
        ),
    ]