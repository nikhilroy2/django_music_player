# Generated by Django 3.2.2 on 2021-05-10 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0018_albummusic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummusic',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='music_list', to='music_app.albumcategory'),
        ),
    ]
