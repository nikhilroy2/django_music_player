from typing import OrderedDict
from django.shortcuts import render, redirect
from .models import NewMp3, PopularMusic, FavoriteMusic,AlbumMusic,AlbumCategory
from music_app import models


#................User Auth .................
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth.models import User

#................User Auth .................End

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
    set_artist = ''
    for music in music_self_list:
        set_artist = music.artist_name
    #print(set_artist)
    music_artist = AlbumMusic.objects.filter(artist_name=set_artist)
    #print(music_self_list)
    context = {
        "music_self_list": music_self_list,
        "music_artist": music_artist,
        "set_artist": set_artist
    }
    return render(request, 'music_list.html', context)

def ArtistAlphabet(request, pk):
    alphabet_type = str(pk).replace('get_', '')
    music_list = models.AlbumMusic.objects.all()
    artist_name = models.AlbumMusic.objects.filter(artist_alphabet=alphabet_type)
    artist_list = []
    for artist in artist_name:
        artist_list.append(artist.artist_name)
    #print(artist_list)
    context = {
        "alphabet_type": alphabet_type,
        "music_list": music_list,
        "artist_name": artist_name,
        "artist_list": list(dict.fromkeys(artist_list))
    }
    
    #print(artist_name_single)

    return render(request, 'artist_search.html', context)


def ArtistMusic(request, pk):
    artist_name =  pk
    artist_music = models.AlbumMusic.objects.filter(artist_name=pk)
    context = {
        "artist_name": pk,
        "artist_music": artist_music
    }
    return render(request, 'artist_music.html', context)

def SignUpPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, " Your account has Sign Up Successfully {request.user.username}")
                return redirect('/')
            messages.error(request, "Unsuccessful please see errors!")
    form = SignUpForm
    return render(request, 'signup.html', {"signup": form})



def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f'Welcome! You logged in as {username}')
                    return redirect('/')
                else:
                    messages.error(request, 'Invalid username or password')
   
    form = AuthenticationForm()
    return render(request,'login.html', {"login": form})

def LogoutPage(request):
    logout(request)
    messages.success(request, 'You have log out!')
    return redirect('/')