from rest_framework.routers import DefaultRouter
# from player.views import ArtistViewSet, AlbumViewSet, GenreViewSet, \
    # TrackViewSet, LyricsViewSet

router = DefaultRouter()

router.register(r'artist', ArtistViewSet, basename="artist")
router.register(r'album', AlbumViewSet, basename="album")
router.register(r'genre', GenreViewSet, basename="genre")
router.register(r'track', TrackViewSet, basename="track")
router.register(r'lyrics', LyricsViewSet, basename="lyrics")
