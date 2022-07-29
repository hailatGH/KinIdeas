from django.db import models
from django.utils.translation import gettext_lazy as _
from core import validators

# Create your models here.

def Artists_Profile_Images(instance, filename):
    return '/'.join(['Media_Files', 'Artists_Profile_Images', str(instance.artist_name), \
        str(instance.artist_name + " - " + filename)])
    # The directory arrangment will be [media/Artists_Profile_Images/{artist_name}/{filename}]

def Albums_Cover_Images(instance, filename):
    return '/'.join(['Media_Files', 'Albums_Cover_Images', str(instance.artist_id), str(instance.album_title), \
        str(instance.album_title + " - " + filename)])
    # The directory arrangment will be [media/Albums_Profile_Images/{album_title}/{filename}]

def Genres_Cover_Images(instance, filename):
    return '/'.join(['Media_Files', 'Genres_Cover_Images', str(instance.genre_title), \
        str(instance.genre_title + " - " + filename)])
    # The directory arrangment will be [media/Genres_Cover_Images/{genre_title}/{filename}]

def Track_Files(instance, filename):
    return '/'.join(['Media_Files', 'Track_Files', str(instance.artist_id), str(instance.album_id), filename])
    # The directory arrangment will be [media/Track_Files/{track_name}/{filename}]

class Artist(models.Model):
    
    class Meta:
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")
        ordering = ['id']

    artist_name = models.CharField(max_length=100, default=_("Unknown Artist"), null=False, blank=True, unique=True)
    artist_title = models.CharField(max_length=100, default=_("Unknown"), null=False, blank=True)
    artist_cover = models.ImageField(upload_to=Artists_Profile_Images, validators=[validators.validate_image_extension], \
        height_field=None, width_field=None, null=False, blank=False, unique=True)
    artist_description = models.TextField(max_length=1023, blank=True, null=True)
    user_id =  models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%d: %s' % (self.pk, self.artist_name)

class Album(models.Model):
    
    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")
        ordering = ['id']

    album_title = models.CharField(max_length=100, default='Unknown Album', null=False, blank=True, unique=True)
    album_cover = models.ImageField(upload_to=Albums_Cover_Images, validators=[validators.validate_image_extension], \
        height_field=None, width_field=None, null=False, blank=False, unique=True)
    album_description = models.TextField(max_length=1023, blank=True, null=True)
    artist_id = models.ForeignKey(Artist, default=1, related_name='albums', on_delete=models.DO_NOTHING)
    user_id =  models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.album_title)

class Genre(models.Model):

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")
        ordering = ['id']

    genre_title = models.CharField(max_length=100, default='Unknown Genre', null=False, blank=True, unique=True)
    genre_cover = models.ImageField(upload_to=Genres_Cover_Images, validators=[validators.validate_image_extension], \
        height_field=None, width_field=None, null=False, blank=False, unique=True)
    genre_description = models.TextField(blank=True, null=True, max_length=1023)
    user_id =  models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.genre_title)

class Track(models.Model):
    
    class Meta:
        verbose_name = _("Track")
        verbose_name_plural = _("Tracks")
        ordering = ['id']

    track_name = models.CharField(max_length=100, default='Unknown Track', null=False, blank=True, unique=True)
    track_description = models.TextField(blank=True, null=True, max_length=1023)
    track_file = models.FileField(upload_to=Track_Files, validators=[validators.validate_track_extension], null=False, \
        blank=False, unique=True)
    track_status = models.BooleanField(default=False)
    track_release_date=models.DateTimeField()
    artist_id = models.ForeignKey(Artist, default=1, related_name='tracks_ar', on_delete=models.DO_NOTHING)
    album_id = models.ForeignKey(Album, default=1, related_name='tracks_al', on_delete=models.DO_NOTHING)
    genre_id = models.ForeignKey(Genre, default=1, related_name='tracks_g', on_delete=models.DO_NOTHING)
    user_id =  models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.track_name)

class Lyrics(models.Model):

    class Meta:
        verbose_name = _("Lyrics")
        verbose_name_plural = _("Lyrics")
        ordering = ['id']

    lyrics_title = models.CharField(max_length=100, default='Unknown Lyrics', null=False, blank=True)
    lyrics_detail = models.TextField(blank=True, null=False, unique=True)
    track_id = models.ForeignKey(Track, default=1, related_name='lyrics', on_delete=models.CASCADE, unique=True)
    user_id =  models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.lyrics_title)

class PlayList(models.Model):

    class Meta:
        verbose_name = _("PlayList")
        verbose_name_plural = _("PlayLists")
        ordering = ['id']
    
    playlist_name = models.CharField(max_length=100, default='Unknown PlayList', null=False, blank=False)
    user_id =  models.IntegerField(default=1, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%d: %s' % (self.pk, self.playlist_name)

class PlayListTracks(models.Model):

    class Meta:
        verbose_name = _("PlayListTrack")
        verbose_name_plural = _("PlayListTracks")
        ordering = ['id']
    
    playlist_id = models.ForeignKey(PlayList, default=1, related_name='playlist_na', on_delete=models.CASCADE, \
        null=False, blank=False)
    track_id = models.ForeignKey(Track, default=1, related_name='playlist_t', on_delete=models.CASCADE, null=False, \
        blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%d: %s' % (self.pk)

class Favourites(models.Model):

    class Meta:
        verbose_name = _("FavouriteList")
        verbose_name_plural = _("FavouriteLists")
        ordering = ['id']
    
    track_id = models.ForeignKey(Track, default=1, related_name='favouritelist', on_delete=models.CASCADE, \
        null=False, blank=False)
    user_id =  models.IntegerField(default=1, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return '%d: %d' % (self.pk, self.user_id)
        return f'{self.pk} {self.user_id}'