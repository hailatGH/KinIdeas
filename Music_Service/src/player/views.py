from requests import Response
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import MusicArtist, MusicAlbum, MusicGenre, MusicTrack, MusicLyrics, MusicPlayList, MusicPlayListTracks, MusicFavourites
from .serializers import ArtistSerializer, AlbumSerializer, GenreSerializer, TrackSerializer, \
    LyricsSerializer, FavouritesSerializer, PlayListSerializer, PlayListTracksSerializer

# Pagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

# Create your views here.

class ArtistViewSet(viewsets.ModelViewSet):
    
    queryset = MusicArtist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = StandardResultsSetPagination

class AlbumViewSet(viewsets.ModelViewSet):
    
    queryset = MusicAlbum.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = StandardResultsSetPagination

class GenreViewSet(viewsets.ModelViewSet):
    
    queryset = MusicGenre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = StandardResultsSetPagination

class TrackViewSet(viewsets.ModelViewSet):
    
    queryset = MusicTrack.objects.all()
    serializer_class = TrackSerializer
    pagination_class = StandardResultsSetPagination


class LyricsViewSet(viewsets.ModelViewSet):
    
    queryset = MusicLyrics.objects.all()
    serializer_class = LyricsSerializer
    pagination_class = StandardResultsSetPagination

class PlayListViewSet(viewsets.ModelViewSet):
    
    queryset = MusicPlayList.objects.all()
    serializer_class = PlayListSerializer
    pagination_class = StandardResultsSetPagination

class PlayListTracksViewSet(viewsets.ModelViewSet):
    
    queryset = MusicPlayListTracks.objects.all()
    serializer_class = PlayListTracksSerializer
    pagination_class = StandardResultsSetPagination

class FavouritesViewSet(viewsets.ModelViewSet):

    queryset = MusicFavourites.objects.all()
    serializer_class = FavouritesSerializer
    pagination_class = StandardResultsSetPagination