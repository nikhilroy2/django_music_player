# Generated by Django 3.2.2 on 2021-05-09 01:25

from django.db import migrations, models
import music_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0016_alter_musiclist_upload_music'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musiclist',
            name='upload_music',
            field=models.FileField(upload_to=music_app.models.MusicList.file_location),
        ),
    ]
