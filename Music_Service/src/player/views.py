from rest_framework import viewsets

# Create your views here.

from .models import Artist, Album, Genre, Track, Lyrics
from .serializers import ArtistSerializer, AlbumSerializer, GenreSerializer, LyricsSerializer, TrackSerializer, \
    GenreSerializer, TrackSerializer, LyricsSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class GenreViewSet(viewsets.ModelViewSet):
    
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class TrackViewSet(viewsets.ModelViewSet):
    
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class LyricsViewSet(viewsets.ModelViewSet):
    
    queryset = Lyrics.objects.all()
    serializer_class = LyricsSerializer