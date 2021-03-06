# Generated by Django 3.2.2 on 2021-05-09 01:48

from django.db import migrations, models
import django.db.models.deletion
import music_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0017_alter_musiclist_upload_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumMusic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.CharField(max_length=500)),
                ('artist_name', models.CharField(default='', max_length=50)),
                ('artist_alphabet', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y'), ('Z', 'Z')], default='A', max_length=2)),
                ('upload_music', models.FileField(upload_to=music_app.models.AlbumMusic.file_location)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.albumcategory')),
            ],
        ),
    ]
