# Generated by Django 3.2.2 on 2021-05-09 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0013_alter_musiclist_upload_music'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musiclist',
            name='upload_music',
            field=models.FileField(upload_to='<function upload_location at 0x000002897A3DD8B0>'),
        ),
    ]
