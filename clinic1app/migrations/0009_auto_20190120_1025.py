# Generated by Django 2.1.5 on 2019-01-20 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic1app', '0008_auto_20190117_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
