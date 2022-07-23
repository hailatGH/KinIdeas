from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Artist, Album, Genre, Track, Lyrics, PlayList, FavouriteList
from .serializers import ArtistSerializer, AlbumSerializer, GenreSerializer, TrackSerializer, \
    LyricsSerializer, PlayListSerializer, FavouriteListSerializer

# Pagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

# Create your views here.

class ArtistViewSet(viewsets.ModelViewSet):
    
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = StandardResultsSetPagination

class AlbumViewSet(viewsets.ModelViewSet):
    
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = StandardResultsSetPagination

class GenreViewSet(viewsets.ModelViewSet):
    
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = StandardResultsSetPagination

class TrackViewSet(viewsets.ModelViewSet):
    
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    pagination_class = StandardResultsSetPagination

class LyricsViewSet(viewsets.ModelViewSet):
    
    queryset = Lyrics.objects.all()
    serializer_class = LyricsSerializer
    pagination_class = StandardResultsSetPagination

class PlayListViewSet(viewsets.ModelViewSet):
    
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer
    pagination_class = StandardResultsSetPagination

class FavouriteListViewSet(viewsets.ModelViewSet):
    
    queryset = FavouriteList.objects.all()
    serializer_class = FavouriteList
    pagination_class = StandardResultsSetPagination