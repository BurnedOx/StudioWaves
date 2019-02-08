from django.urls import path
from . import views

app_name = 'works'
urlpatterns = [
    path('', views.index, name='index'),
    path('<song_title>/', views.SpecificSong, name='SpecificSong'),
    path('artist/<artist_name>/', views.SpecificArtist, name='SpecificArtist'),
    path('album/<album_id>[0-9]/', views.SpecificAlbum, name='SpecificAlbum'),
]
