# Generated by Django 3.2.2 on 2021-05-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0003_auto_20210507_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musiclist',
            name='upload_music',
            field=models.FileField(upload_to=''),
        ),
    ]