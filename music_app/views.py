from django.shortcuts import render
from .models import MusicList, AlbumCategory
# Create your views here.
def Index(request):
    context = {
        "music_list": MusicList.objects.all()
    }
    print(MusicList.objects.all())
    return render(request, 'index.html', {"context": context})