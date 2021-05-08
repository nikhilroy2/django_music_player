from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index, name="index"),
    path('music_view/<str:pk>', views.MusicList, name="music_view")
]