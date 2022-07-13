from rest_framework.routers import DefaultRouter

from player.views import PlaylistViewSet, FavouriteViewSet

router = DefaultRouter()

# Playlist URLs
router.register(r'playlist', PlaylistViewSet, basename="playlist")

# Favourite URLs
router.register(r'favourite', FavouriteViewSet, basename="favourite")