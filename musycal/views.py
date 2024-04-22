from django.shortcuts import redirect, render
from django.urls import reverse

from musycal.models import Musician, Album, Song

# Create your views here.
def musicians(request):
    artists = Musician.objects.all()
    context = {
        'musicians': artists
    }
    return render(request, 'musycal/musicians.html', context)

def musician_details(request, id):
    details = Musician.objects.get(pk=id)
    albums = Album.objects.filter(artist=details)
    songs = Song.objects.filter(album__artist=details)
    context = {
        'musician': details,
        'albums': albums,
        'songs': songs
    }

    return render(request, 'musycal/musician_details.html', context)

def albums(request):
    return render(request, 'musycal/albums.html')

def album_details(request, id):
    return render(request, 'musycal/album_details.html')

def songs(request):
    return render(request, 'musycal/songs.html')

def song_details(request, id):
    #return redirect(reverse('song_details', args=[id]))
    return render(request, 'musycal/song_details.html')
