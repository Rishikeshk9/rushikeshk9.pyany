# Generated by Django 3.0.2 on 2020-04-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidManager', '0004_auto_20200416_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='covidiot',
            name='lat',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='covidiot',
            name='lon',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]