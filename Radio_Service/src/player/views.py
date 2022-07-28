from rest_framework import viewsets

from .models import Station
from .serializers import StationSerializer

# Create your views here.

class RadioViewSet(viewsets.ModelViewSet):
    
    queryset = Station.objects.all()
    serializer_class = StationSerializer