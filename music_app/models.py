from django.db import models
from os.path import join as osjoin
# from django.dispatch import receiver
# Create your models here.


Alphabet_Choices = [
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    ('E','E'),
    ('F','F'),
    ('G','G'),
    ('H','H'),
    ('I','I'),
    ('J','J'),
    ('K','K'),
    ('L','L'),
    ('M','M'),
    ('N','N'),
    ('O','O'),
    ('P','P'),
    ('Q','Q'),
    ('R','R'),
    ('S','S'),
    ('T','T'),
    ('U','U'),
    ('V','V'),
    ('W','W'),
    ('X','X'),
    ('Y','Y'),
    ('Z','Z'),
]


class AlbumCategory(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.category_name)

def image_path(instance, filename):
    pass
    #return '/'.join(['uploads', instance.category_name.pk, filename])

def upload_location(instance, filename):
    pass
    #print(AlbumCategory)
    #return (AlbumCategory, filename)

class MusicList(models.Model):
    def file_location(self, filename):
        return osjoin(str(self.category_name), filename)

    music_name = models.CharField(max_length=500)
    artist_name = models.CharField(max_length=50, default='')
    artist_alphabet = models.CharField(max_length=2, choices=Alphabet_Choices, default='A')
    category_name = models.ForeignKey(AlbumCategory,on_delete=models.CASCADE, null=False)
    upload_music = models.FileField(upload_to=file_location)
    def get_upload_path(instance, filename):
        pass
        #return '{0}/{1}'.format(instance.AlbumCategory.category_name, filename)
    
    def image_dir(self, filename):
        pass
        #return osjoin(str(self.category_name), filename)

    def __str__(self):
        return str(self.music_name)
    


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




class AlbumMusic(models.Model):
    def file_location(self, filename):
        return osjoin(str(self.category_name), filename)
    music_name = models.CharField(max_length=500)
    artist_name = models.CharField(max_length=50, default='')
    artist_alphabet = models.CharField(max_length=2, choices=Alphabet_Choices, default='A')
    category_name = models.ForeignKey(AlbumCategory,on_delete=models.CASCADE,  related_name="music_list", null=True,  db_column="category_column",)
    upload_music = models.FileField(upload_to=file_location)
    upload_thumbnail = models.ImageField(upload_to=file_location, null=True, blank=True)
    #numdownload = models.IntegerField(null=True,default=0, editable=False)
    # def increment_numdownload(self):
    #     self.numdownload +=1
    #     return self.numdownload
        
    def __str__(self):
        return str(self.music_name)


