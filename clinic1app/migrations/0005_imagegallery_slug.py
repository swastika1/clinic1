# Generated by Django 2.1.5 on 2019-01-09 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic1app', '0004_auto_20190109_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagegallery',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
