from rest_framework.routers import DefaultRouter

from player.views import StationViewSet, FavouriteViewSet

router = DefaultRouter()

router.register(r'station', StationViewSet, basename="station")
router.register(r'favourites', FavouriteViewSet, basename="favourites")