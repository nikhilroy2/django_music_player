# Generated by Django 3.2.2 on 2021-05-13 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0027_albummusic_numdownload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albummusic',
            name='numdownload',
        ),
    ]
