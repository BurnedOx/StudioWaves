from django.urls import path
from . import views

app_name = 'works'
urlpatterns = [
    path('', views.index, name='index'),
    path('<song_title>/', views.SpecificSong, name='SpecificSong'),
    path('artist/<artist_name>/', views.SpecificArtist, name='SpecificArtist'),
    path('artist/album/<album_id>/', views.SpecificAlbum, name='SpecificAlbum'),
]