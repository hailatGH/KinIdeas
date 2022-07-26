from requests import Response
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Artist, Album, Genre, Track, Lyrics, PlayList, PlayListTracks, Favourites
from .serializers import ArtistSerializer, AlbumSerializer, GenreSerializer, TrackSerializer, \
    LyricsSerializer, FavouritesSerializer, PlayListSerializer, PlayListTracksSerializer

# Pagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

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

class PlayListTracksViewSet(viewsets.ModelViewSet):
    
    serializer_class = PlayListTracksSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        id = self.request.query_params['id']
        queryset = PlayListTracks.objects.filter(playlist_id=id)

        return queryset

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

class FavouritesViewSet(viewsets.ModelViewSet):
    
    serializer_class = FavouritesSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        id = self.request.query_params['id']
        queryset = Favourites.objects.filter(user_id=id)

        return queryset

    def perform_destroy(self, instance): 
        super().perform_destroy(instance)