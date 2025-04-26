from django.shortcuts import render
from .models import Band, Album, Artist, Song

def bands_view(request):
    bands = Band.objects.all()
    return render(request, 'main/kapely.html', {'bands': bands})

def albums_view(request):
    albums = Album.objects.all()
    return render(request, 'main/alba.html', {'albums': albums})

def artists_view(request):
    artists = Artist.objects.all()
    return render(request, 'main/clenove.html', {'artists': artists})

def songs_view(request):
    songs = Song.objects.all()
    return render(request, 'main/skladby.html', {'songs': songs})




