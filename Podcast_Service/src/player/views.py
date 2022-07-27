from requests import Response
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Host, Season, PodcastCategory, Episode, PlayList, PlayListEpisodes, Favourites
from .serializers import HostSerializer, SeasonSerializer, PodcastCategorySerializer, EpisodeSerializer,\
    PlayListSerializer, PlayListEpisodesSerializer, FavouritesSerializer

# Pagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

# Create your views here.

class HostViewSet(viewsets.ModelViewSet):
    
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class SeasonViewSet(viewsets.ModelViewSet):
    
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class PodcastCategoryViewSet(viewsets.ModelViewSet):
    
    queryset = PodcastCategory.objects.all()
    serializer_class = PodcastCategorySerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class PlayListViewSet(viewsets.ModelViewSet):
    
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer
    pagination_class = StandardResultsSetPagination

class PlayListEpisodesViewSet(viewsets.ModelViewSet):
    
    queryset = PlayListEpisodes.objects.all()
    serializer_class = PlayListEpisodesSerializer
    pagination_class = StandardResultsSetPagination

class FavouritesViewSet(viewsets.ModelViewSet):

    queryset = Favourites.objects.all()
    serializer_class = FavouritesSerializer
    pagination_class = StandardResultsSetPagination