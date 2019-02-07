from django.db import models

# Create your models here.

class Artist(models.Model):
    artist_name = models.CharField(max_length=250)
    place = models.CharField(max_length=100)
    artist_logo = models.FileField()

    def __str__(self):
        return self.artist_name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.album_title + ' - ' + self.artist.artist_name

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=None)
    song_title = models.CharField(max_length=250)
    audio_track = models.FileField()

    def __str__(self):
        return self.song_title

class Gallery(models.Model):
    pic_name = models.CharField(max_length=200)
    pic = models.FileField()
    about = models.CharField(max_length=500, default=None)

    def __str__(self):
        return self.pic_name

class Video(models.Model):
    link = models.CharField(max_length=10000)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.link
