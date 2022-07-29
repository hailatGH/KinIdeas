from requests import Response
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import PodcastHost, PodcastSeason, PodcastCategory, PodcastEpisode, PodcastPlayList, PodcastPlayListEpisodes, PodcastFavourites
from .serializers import HostSerializer, SeasonSerializer, PodcastCategorySerializer, EpisodeSerializer,\
    PlayListSerializer, PlayListEpisodesSerializer, FavouritesSerializer

# Pagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

# Create your views here.

class HostViewSet(viewsets.ModelViewSet):
    
    queryset = PodcastHost.objects.all()
    serializer_class = HostSerializer

class SeasonViewSet(viewsets.ModelViewSet):
    
    queryset = PodcastSeason.objects.all()
    serializer_class = SeasonSerializer

class PodcastCategoryViewSet(viewsets.ModelViewSet):
    
    queryset = PodcastCategory.objects.all()
    serializer_class = PodcastCategorySerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    
    queryset = PodcastEpisode.objects.all()
    serializer_class = EpisodeSerializer

class PlayListViewSet(viewsets.ModelViewSet):
    
    queryset = PodcastPlayList.objects.all()
    serializer_class = PlayListSerializer
    pagination_class = StandardResultsSetPagination

class PlayListEpisodesViewSet(viewsets.ModelViewSet):
    
    queryset = PodcastPlayListEpisodes.objects.all()
    serializer_class = PlayListEpisodesSerializer
    pagination_class = StandardResultsSetPagination

class FavouritesViewSet(viewsets.ModelViewSet):

    queryset = PodcastFavourites.objects.all()
    serializer_class = FavouritesSerializer
    pagination_class = StandardResultsSetPagination