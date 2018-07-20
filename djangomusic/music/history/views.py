from django.shortcuts import render
from django.http import HttpResponse


def artists(request):
    artist_list = Artist.objects.all()
    print("artist list??", artist_list)
    context = {"artists": artist_list}
    return render(request, 'history/artists.html', context)

def new_artist(request):
    print(request.POST)

def detail(request, artist_id):
    print("this is a detail request")
    artist = get_object_or_404(Artist, pk=artist_id)
    songs = artist.song_set.all()