# Generated by Django 3.0.5 on 2020-06-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_currentimages_programstarted'),
    ]

    operations = [
        migrations.AddField(
            model_name='trafficlight',
            name='emergency',
            field=models.BooleanField(default=False),
        ),
    ]
