from django.db import models
from django.utils.translation import gettext_lazy as _
from core import validators
from core.settings import MEDIA_ROOT

def artists_cover_images(instance, filename):
    return '/'.join(['artists_cover_images', str(instance.artist_name), filename])
    # The directory arrangment will be [Media/artists_cover_images/{artist_name}/{filename}]

def albums_cover_images(instance, filename):
    return '/'.join(['albums_cover_images', str(instance.album_title), filename])
    # The directory arrangment will be [Media/albums_cover_images/{album_title}/{filename}]

def genres_cover_images(instance, filename):
    return '/'.join(['genres_cover_images', str(instance.genre_title), filename])
    # The directory arrangment will be [Media/genres_cover_images/{genre_title}/{filename}]

def track_files(instance, filename):
    return '/'.join(['track_files', str(instance.track_name), filename])
    # The directory arrangment will be [Media/track_files/{track_name}/{filename}]

class Artist(models.Model):
    
    class Meta:
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")
        ordering = ['id']

    artist_name = models.CharField(max_length=100, default=_("unknown"), null=False, blank=False)
    artist_title = models.CharField(max_length=100, default=_("unknown"), null=False, blank=False)
    artist_cover = models.ImageField(upload_to=artists_cover_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=1023, null=False, blank=False)
    artist_description = models.TextField(max_length=1023, blank=True, null=True)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%d: %s' % (self.pk, self.artist_name)


class Album(models.Model):
    
    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")
        ordering = ['id']

    album_title = models.CharField(max_length=100, default='Collections', null=False, blank= False)
    album_cover = models.ImageField(upload_to=albums_cover_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=1023, null=False, blank=False)
    album_description = models.TextField(max_length=1023, blank=True, null=True)
    artist_id = models.ForeignKey(Artist, default=0, related_name='albums', on_delete=models.DO_NOTHING)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.album_title)

class Genre(models.Model):

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")
        ordering = ['id']

    genre_title = models.CharField(max_length=100,default='Other',null=False , blank= False)
    genre_cover = models.ImageField(upload_to=genres_cover_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=1023, null=False, blank=False)
    genre_description = models.TextField(blank=True, null=True, max_length=1023)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.genre_title)

class Track(models.Model):
    
    class Meta:
        verbose_name = _("Track")
        verbose_name_plural = _("Tracks")
        ordering = ['id']

    track_name = models.CharField(max_length=120, default='Unknown_track',null=False, blank= False)
    track_description = models.TextField(blank=True, null=True, max_length=1023)
    track_file = models.FileField(upload_to=track_files, validators=[validators.validate_track_extension], null=False, blank=False)
    track_status = models.BooleanField(default=False)
    track_release_date=models.DateTimeField()
    album_id = models.ForeignKey(Album, default=0, related_name='tracks_a', on_delete=models.DO_NOTHING)
    genre_id = models.ForeignKey(Genre, default=0, related_name='tracks_g', on_delete=models.DO_NOTHING)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.track_name)

class Lyrics(models.Model):

    class Meta:
        verbose_name = _("Lyrics")
        verbose_name_plural = _("Lyrics")
        ordering = ['id']

    lyrics_title = models.CharField(max_length=100,default='Other',null=False , blank= False)
    lyrics_detail = models.TextField(blank=True, null=True, max_length=1023)
    track_id = models.ForeignKey(Track, default=0, related_name='lyrics', on_delete=models.DO_NOTHING)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.lyrics_title)