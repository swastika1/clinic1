# Generated by Django 2.1.5 on 2019-01-09 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic1app', '0003_auto_20190109_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='image',
            field=models.ImageField(upload_to='facility/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='services/'),
        ),
    ]
