from rest_framework import viewsets
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

from .models import Artist, Album, Genre, Track, Lyrics
from .serializers import ArtistSerializer, AlbumSerializer, \
    GenreSerializer, TrackSerializer, LyricsSerializer

# Create your views here.

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

class MusicPlayerAPIView(ObjectMultipleModelAPIViewSet):
    querylist = [
        {'queryset': Artist.objects.all(), 'serializer_class': ArtistSerializer},
        {'queryset': Album.objects.all(), 'serializer_class': AlbumSerializer},
        {'queryset': Genre.objects.all(), 'serializer_class': GenreSerializer},
        {'queryset': Track.objects.all(), 'serializer_class': TrackSerializer},
        {'queryset': Lyrics.objects.all(), 'serializer_class': LyricsSerializer},
    ]