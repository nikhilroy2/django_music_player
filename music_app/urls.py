from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index, name="index"),
    path('music_view/<str:pk>', views.MusicList, name="music_view"),
    path('artist_alphabet/<str:pk>', views.ArtistAlphabet, name="artist_alphabet"),
    path('artist_music/<str:pk>', views.ArtistMusic, name="artist_music"),
]