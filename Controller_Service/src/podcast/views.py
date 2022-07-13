from rest_framework import viewsets

from .models import Host, Season, PodcastCategory, Episode 
from .serializers import HostSerializer, SeasonSerializer, \
    PodcastCategorySerializer, EpisodeSerializer

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