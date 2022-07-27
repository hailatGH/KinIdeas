from django.db import models
from django.utils.translation import gettext_lazy as _
from core import validators

def Hosts_Profile_Images(instance, filename):
    return '/'.join(['Media_Files', 'Hosts_Profile_Images', str(instance.host_name),\
        str(instance.host_name + " - " + filename)])
    # The directory arrangment will be [Media/hosts_cover_images/{host_name}/{filename}]

def Seasons_Cover_Images(instance, filename):
    return '/'.join(['Media_Files', 'Seasons_Cover_Images', str(instance.season_title),\
         str(instance.season_title + " - " + filename)])
    # The directory arrangment will be [Media/seasons_cover_images/{season_title}/{filename}]

def Podcast_Categorys_Cover_Images(instance, filename):
    return '/'.join(['Media_Files', 'Podcast_Categorys_Cover_Images', str(instance.podcast_category_title),\
        str(instance.podcast_category_title + " - " + filename)])
    # The directory arrangment will be [Media/podcast_categorys_cover_images/{podcast_category_title}/{filename}]

def Episode_Files(instance, filename):
    return '/'.join(['Media_Files', 'Episode_Files', str(instance.episode_title),\
        str(instance.episode_title + " - " + filename)])
    # The directory arrangment will be [Media/episode_files/{episode_title}/{filename}]

class Host(models.Model):
    
    class Meta:
        verbose_name = _("Host")
        verbose_name_plural = _("Hosts")
        ordering = ['id']

    host_name = models.CharField(max_length=100, default=_("Unknown Host"), null=False, blank=True, unique=True)
    host_title = models.CharField(max_length=100, default=_("Unknown"), null=False, blank=True)
    host_cover = models.ImageField(upload_to=Hosts_Profile_Images, validators=[validators.validate_image_extension], \
        height_field=None, width_field=None, null=False, blank=True, unique=True)
    host_description = models.TextField(max_length=1023, blank=True, null=True)
    user_id =  models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%d: %s' % (self.pk, self.host_name)


class Season(models.Model):
    
    class Meta:
        verbose_name = _("Season")
        verbose_name_plural = _("Seasons")
        ordering = ['id']

    season_title = models.CharField(max_length=100, default='Unknown Season', null=False, blank=True, unique=True)
    season_cover = models.ImageField(upload_to=Seasons_Cover_Images, validators=[validators.validate_image_extension], \
        height_field=None, width_field=None, null=False, blank=True, unique=True)
    season_description = models.TextField(max_length=1023, blank=True, null=True)
    host_id = models.ForeignKey(Host, default=1, related_name='seasons', on_delete=models.DO_NOTHING)
    user_id =  models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.season_title)

class PodcastCategory(models.Model):

    class Meta:
        verbose_name = _("PodcastCategory")
        verbose_name_plural = _("PodcastCategories")
        ordering = ['id']

    podcast_category_title = models.CharField(max_length=100, default='Unknown Genre', null=False, blank=True, unique=True)
    podcast_category_cover = models.ImageField(upload_to=Podcast_Categorys_Cover_Images, validators=[validators.validate_image_extension], \
        height_field=None, width_field=None, null=False, blank=True, unique=True)
    podcast_category_description = models.TextField(blank=True, null=True, max_length=1023)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.podcast_category_title)

class Episode(models.Model):
    
    class Meta:
        verbose_name = _("Episode")
        verbose_name_plural = _("Episodes")
        ordering = ['id']

    episode_title = models.CharField(max_length=100, default='Unknown Episode', null=False, blank=True, unique=True)
    episode_description = models.TextField(blank=True, null=True, max_length=1023)
    episode_file = models.FileField(upload_to=Episode_Files, validators=[validators.validate_track_extension], null=False, \
        blank=True, unique=True)
    episode_status = models.BooleanField(default=False)
    episode_release_date=models.DateTimeField()
    host_id = models.ForeignKey(Host, default=1, related_name='episode_h', on_delete=models.DO_NOTHING)
    season_id = models.ForeignKey(Season, default=1, related_name='episode_s', on_delete=models.DO_NOTHING)
    podcast_category_id = models.ForeignKey(PodcastCategory, default=1, related_name='episode_c', on_delete=models.DO_NOTHING)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.episode_title)

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
    episode_id = models.ForeignKey(Episode, default=1, related_name='playlist_e', on_delete=models.CASCADE, null=False, \
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
    
    episode_id = models.ForeignKey(Episode, default=1, related_name='favouritelist', on_delete=models.CASCADE, \
        null=False, blank=False)
    user_id =  models.IntegerField(default=1, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%d: %d' % (self.pk, self.user_id)