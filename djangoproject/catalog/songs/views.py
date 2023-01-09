from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Song

# Create your views here.

def index(request):
    songs = Song.objects.all()

    context = {
        'songs': songs     
    }
    return render(request, 'songs/list.html',context)

def detail(request, song_id):
    song = get_object_or_404(Song, pk = song_id)
    context = {
        'song':song
    }
    return render(request, 'songs/detail.html',context)

def search(request):
    return render(request, 'songs/search.html')