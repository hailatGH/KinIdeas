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

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.artist_cover:
            artist_cover = Artist.objects.filter(id=instance.id).values('artist_cover')[0]['artist_cover']
            # print(artist_cover)
            instance.artist_cover = artist_cover

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

class AlbumViewSet(viewsets.ModelViewSet):
    
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        album_title = serializer.validated_data.get('album_title') or None
        if album_title is None:
            album_title = "Unknown Album"
        serializer.save(album_title=album_title)

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

class GenreViewSet(viewsets.ModelViewSet):
    
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        genre_title = serializer.validated_data.get('genre_title') or None
        if genre_title is None:
            genre_title = "Unknown Genre"
        serializer.save(genre_title=genre_title)
    
    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

class TrackViewSet(viewsets.ModelViewSet):
    
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    pagination_class = StandardResultsSetPagination

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

class LyricsViewSet(viewsets.ModelViewSet):
    
    queryset = Lyrics.objects.all()
    serializer_class = LyricsSerializer
    pagination_class = StandardResultsSetPagination

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

class PlayListViewSet(viewsets.ModelViewSet):
    
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer
    pagination_class = StandardResultsSetPagination

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

class FavouriteListViewSet(viewsets.ModelViewSet):
    
    queryset = FavouriteList.objects.all()
    serializer_class = FavouriteListSerializer
    pagination_class = StandardResultsSetPagination

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)