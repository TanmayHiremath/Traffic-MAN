# Generated by Django 3.0.5 on 2020-06-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_image_sn'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img0', models.IntegerField(default=1)),
                ('img1', models.IntegerField(default=1)),
                ('img2', models.IntegerField(default=1)),
                ('img3', models.IntegerField(default=1)),
            ],
        ),
    ]
