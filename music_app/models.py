from django.db import models
# from django.dispatch import receiver
# Create your models here.
class AlbumCategory(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name or ''

class MusicList(models.Model):
    name = models.CharField(max_length=500)
    category_name = models.ForeignKey(AlbumCategory,on_delete=models.CASCADE)
    upload_music = models.FileField()
    def __str__(self):
        return self.category_name or ''
    


class NewMp3(models.Model):
    upload_music = models.FileField(upload_to='NewMp3')
    def __str__(self):
        return str(self.upload_music).replace('NewMp3/','')
 

class PopularMusic(models.Model):
    upload_music = models.FileField(upload_to='PopularMusic')
    def __str__(self):
        return str(self.upload_music).replace('PopularMusic/','')

 

class FavoriteMusic(models.Model):
    upload_music = models.FileField(upload_to='FavoriteMusic',)
    def __str__(self):
        return str(self.upload_music).replace('FavoriteMusic/','')
 

# @receiver(models.signals.pre_delete, sender=NewMp3)
# def remove_file_from_s3(sender, instance, using, **kwargs):
#    instance.image_file.delete(save=False)