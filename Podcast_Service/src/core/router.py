from rest_framework.routers import DefaultRouter

from player.views import HostViewSet, SeasonViewSet, PodcastCategoryViewSet, EpisodeViewSet, FavouritesViewSet, \
    PlayListViewSet, PlayListEpisodesViewSet

router = DefaultRouter()

router.register(r'host', HostViewSet, basename="host")
router.register(r'season', SeasonViewSet, basename="season")
router.register(r'category', PodcastCategoryViewSet, basename="category")
router.register(r'episode', EpisodeViewSet, basename="episode")
router.register(r'playlists', PlayListViewSet, basename="playlists")
router.register(r'playlisttracks', PlayListEpisodesViewSet, basename="playlisttracks")
router.register(r'favourites', FavouritesViewSet, basename="favourites")