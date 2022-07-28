from rest_framework.routers import DefaultRouter

from player.views import StationViewSet 

router = DefaultRouter()

router.register(r'station', StationViewSet, basename="station")