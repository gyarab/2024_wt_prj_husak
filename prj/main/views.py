from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
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

def album_detail_api(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    songs = Song.objects.filter(album=album).values('id', 'title')
    data = {
        "id": album.id,
        "songs": list(songs)
    }
    return JsonResponse(data)

def artist_detail_api(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    bands = Band.objects.filter(bandartist__artist=artist).values('id', 'name')
    data = {
        "id": artist.id,
        "name": artist.name,
        "songs": list(bands)
    }
    return JsonResponse(data)





