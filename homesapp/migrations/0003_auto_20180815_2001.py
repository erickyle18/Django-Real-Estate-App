# Generated by Django 2.1 on 2018-08-16 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesapp', '0002_auto_20180815_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='lat_field',
            field=models.CharField(default='NA', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='long_field',
            field=models.CharField(default='NA', max_length=200),
            preserve_default=False,
        ),
    ]
