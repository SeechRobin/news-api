# Generated by Django 2.0.4 on 2018-04-25 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_api', '0005_auto_20180425_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='review',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='title',
        ),
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(),
        ),
    ]
