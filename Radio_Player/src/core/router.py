from rest_framework.routers import DefaultRouter

from player.views import FavouriteViewSet

router = DefaultRouter()

# Favourite URLs
router.register(r'favourite', FavouriteViewSet, basename="favourite")