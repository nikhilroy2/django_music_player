from django.db import models

# Create your models here.
class AlbumCategory(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class MusicList(models.Model):
    name = models.CharField(max_length=500)
    category_name = models.ForeignKey(AlbumCategory,on_delete=models.CASCADE)
    upload_music = models.FileField()
    def __str__(self):
        return self.category_name
    