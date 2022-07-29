from rest_framework import viewsets

from .models import RadioStation, RadioStationFavourites
from .serializers import StationSerializer, FavouritesSerializer

# Create your views here.

class StationViewSet(viewsets.ModelViewSet):
    
    queryset = RadioStation.objects.all()
    serializer_class = StationSerializer

class FavouriteViewSet(viewsets.ModelViewSet):
    
    queryset = RadioStationFavourites.objects.all()
    serializer_class = FavouritesSerializer