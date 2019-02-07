from django.shortcuts import render, get_object_or_404, redirect
from .models import Artist, Album, Song, Gallery, Video
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def SendEmail(form):
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    message = form.cleaned_data['message']

    subject = 'Contact Form Received'
    from_email = settings.EMAIL_HOST_USER
    to_email = [from_email]
    contact_message = """
            MESSAGE: {0}
            FROM: {1}
            EMAIL {2}""".format(message, name, email)

    send_mail(subject, contact_message, from_email, to_email, fail_silently=False)

def index(request):
    all_artists = Artist.objects.all()
    all_albums = Album.objects.all()
    all_songs = Song.objects.all()
    gallery = Gallery.objects.all()
    videos = Video.objects.all()

    form = ContactForm(request.POST)
    if form.is_valid():
        SendEmail(form)
        return redirect('/')

    context = {
        'all_artists': all_artists,
        'all_albums': all_albums,
        'all_songs': all_songs,
        'form': form,
        'gallery': gallery,
        'videos': videos,
    }

    return render(request, 'works/index.html', context)

def SpecificSong(request, song_title):
    song = Song.objects.get(song_title=song_title)

    form = ContactForm(request.POST)
    if form.is_valid():
        SendEmail(form)
        return redirect('/' + song_title + '/')

    context = {
        'song': song,
        'form': form,
    }
    return render(request, 'works/specificsong.html', context)

def SpecificArtist(request, artist_name):
    artist = Artist.objects.get(artist_name=artist_name)

    form = ContactForm(request.POST)
    if form.is_valid():
        SendEmail(form)
        return redirect('/artist/' + artist_name + '/')

    context = {
        'artist': artist,
        'form': form,
    }
    return render(request, 'works/specificartist.html', context)

def SpecificAlbum(request, album_id):
    album = Album.objects.get(id=album_id)

    form = ContactForm(request.POST)
    if form.is_valid():
        SendEmail(form)
        return redirect('/artist/album/' + album_id + '/')

    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'works/specificalbum.html', context)


