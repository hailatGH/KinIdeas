from rest_framework import viewsets

from .models import Favourite, Playlist
from .serializers import FavouriteSerializer, PlaylistSerializer

# Create your views here.

class FavouriteViewSet(viewsets.ModelViewSet):
    
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer

# Create your views here.

class PlaylistViewSet(viewsets.ModelViewSet):
    
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer