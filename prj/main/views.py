from django.shortcuts import render
from .models import Album

def albums_view(request):
    albums = Album.objects.all()
    return render(request, 'main/alba.html', {'albums': albums})




