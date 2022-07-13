from rest_framework import viewsets

from .models import Radio
from .serializers import RadioSerializer

# Create your views here.

class RadioViewSet(viewsets.ModelViewSet):
    
    queryset = Radio.objects.all()
    serializer_class = RadioSerializer