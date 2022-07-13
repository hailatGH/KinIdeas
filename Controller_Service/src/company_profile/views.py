from rest_framework import viewsets

from .models import CompanyProfile
from .serializers import CompanyProfileSerializer

# Create your views here.

class CompanyProfileViewSet(viewsets.ModelViewSet):
    
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer