# Generated by Django 3.1.5 on 2021-01-26 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pairs', '0003_auto_20210127_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pair',
            name='orientation',
            field=models.CharField(choices=[('NS', 'North/South'), ('EW', 'East/West')], default='EW', max_length=2),
        ),
    ]
