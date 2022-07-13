from rest_framework import viewsets

from .models import Favourite
from .serializers import FavouriteSerializer

# Create your views here.

class FavouriteViewSet(viewsets.ModelViewSet):
    
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer