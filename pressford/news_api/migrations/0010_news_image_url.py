# Generated by Django 2.0.4 on 2018-04-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_api', '0009_auto_20180425_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]