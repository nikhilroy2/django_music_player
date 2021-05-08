from django.shortcuts import render
from .models import NewMp3, PopularMusic, FavoriteMusic
# Create your views here.
def Index(request):
    context = {
        "NewMp3": NewMp3.objects.all(),
        "PopularMusic": PopularMusic.objects.all(),
        "FavoriteMusic": FavoriteMusic.objects.all()
    }
    
    return render(request, 'index.html', {"context": context})



def MusicList(request, pk):
    return render(request, 'music_list.html')