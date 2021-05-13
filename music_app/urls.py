from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path('', views.Index, name="index"),
    path('music_view/<str:pk>', views.MusicList, name="music_view"),
    path('artist_alphabet/<str:pk>', views.ArtistAlphabet, name="artist_alphabet"),
    path('artist_music/<str:pk>', views.ArtistMusic, name="artist_music"),
    path('login', views.LoginPage, name="login"),
    path('signup', views.SignUpPage, name="signup"),
    path('logout', views.LogoutPage, name="logout"),
    path('music_upload', views.MusicUploadPage, name="music_upload"),
    path('search_music', views.SearchPage, name="search_music"),
    # path('download/<str:pk>', views.DownloadCounter, name="download_count")
]



