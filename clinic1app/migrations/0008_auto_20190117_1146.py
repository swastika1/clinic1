# Generated by Django 2.1.5 on 2019-01-17 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic1app', '0007_auto_20190117_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogallery',
            name='video_link',
            field=models.CharField(max_length=100),
        ),
    ]
