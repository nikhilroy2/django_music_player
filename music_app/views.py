from django.shortcuts import render
from .models import NewMp3, PopularMusic, FavoriteMusic,AlbumMusic,AlbumCategory
from music_app import models
# Create your views here.
def Index(request):
    context = {
        "NewMp3": NewMp3.objects.all(),
        "PopularMusic": PopularMusic.objects.all(),
        "FavoriteMusic": FavoriteMusic.objects.all(),
        "AlbumCategory": AlbumCategory.objects.all()
        
    }
    return render(request, 'index.html',context)



def MusicList(request, pk):
    music_name = str(pk).replace('%20', ' ')
    #print(music_name)
    music_self_list = AlbumMusic.objects.filter(music_name=music_name)
    #print(music_self_list)
    context = {
        "music_self_list": music_self_list
    }
    return render(request, 'music_list.html', context)

def ArtistAlphabet(request, pk):
    alphabet_type = str(pk).replace('get_', '')
    music_list = models.AlbumMusic.objects.all()
    artist_name = models.AlbumMusic.objects.filter(artist_alphabet=alphabet_type)
    context = {
        "alphabet_type": alphabet_type,
        "music_list": music_list,
        "artist_name": artist_name
    }

    return render(request, 'artist_search.html', context)


def ArtistMusic(request, pk):
    artist_name =  pk
    artist_music = models.AlbumMusic.objects.filter(artist_name=pk)
    context = {
        "artist_name": pk,
        "artist_music": artist_music
    }
    return render(request, 'artist_music.html', context)