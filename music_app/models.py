from django.db import models

# Create your models here.
class AlbumCategory(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category

class MusicList(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(AlbumCategory,on_delete=models.CASCADE)
    def __str__(self):
        return self.category
    