# Generated by Django 4.0.4 on 2023-01-18 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_api', '0002_alter_music_artist_alter_music_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='artist',
            field=models.CharField(blank=True, default=None, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='thumbnail',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
