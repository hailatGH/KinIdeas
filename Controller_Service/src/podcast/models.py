from django.db import models
from django.utils.translation import gettext_lazy as _

from core import validators
from core.settings import MEDIA_ROOT

def hosts_cover_images(instance, filename):
    return '/'.join(['hosts_cover_images', str(instance.host_name), filename])
    # The directory arrangment will be [Media/hosts_cover_images/{host_name}/{filename}]

def seasons_cover_images(instance, filename):
    return '/'.join(['seasons_cover_images', str(instance.season_title), filename])
    # The directory arrangment will be [Media/seasons_cover_images/{season_title}/{filename}]

def podcast_categorys_cover_images(instance, filename):
    return '/'.join(['podcast_categorys_cover_images', str(instance.podcast_category_title), filename])
    # The directory arrangment will be [Media/podcast_categorys_cover_images/{podcast_category_title}/{filename}]

def episode_files(instance, filename):
    return '/'.join(['episode_files', str(instance.episode_title), filename])
    # The directory arrangment will be [Media/episode_files/{episode_title}/{filename}]

class Host(models.Model):
    
    class Meta:
        verbose_name = _("Host")
        verbose_name_plural = _("Hosts")
        ordering = ['id']

    host_name = models.CharField(max_length=100, default=_("unknown"), null=False, blank=False)
    host_title = models.CharField(max_length=100, default=_("unknown"), null=False, blank=False)
    host_cover = models.ImageField(upload_to=hosts_cover_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=1023, null=False, blank=False)
    host_description = models.TextField(max_length=1023, blank=True, null=True)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%d: %s' % (self.pk, self.host_name)


class Season(models.Model):
    
    class Meta:
        verbose_name = _("Season")
        verbose_name_plural = _("Seasons")
        ordering = ['id']

    season_title = models.CharField(max_length=100, default='Collections', null=False, blank=False)
    season_cover = models.ImageField(upload_to=seasons_cover_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=1023, null=False, blank=False)
    season_description = models.TextField(max_length=100, blank=True, null=True)
    host_id = models.ForeignKey(Host, default=0, related_name='seasons', on_delete=models.DO_NOTHING)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.season_title)

class PodcastCategory(models.Model):

    class Meta:
        verbose_name = _("PodcastCategory")
        verbose_name_plural = _("PodcastCategories")
        ordering = ['id']

    podcast_category_title = models.CharField(max_length=100, default='Other', null=False, blank=False)
    podcast_category_cover = models.ImageField(upload_to=podcast_categorys_cover_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=1023, null=False, blank=False)
    podcast_category_description = models.TextField(max_length=1023, blank=True, null=True)
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

    episode_title = models.CharField(max_length=120, default='Unknown_track', null=False, blank= False)
    episode_description = models.TextField(blank=True, null=True, max_length=1023)
    episode_file = models.FileField(upload_to=episode_files, validators=[validators.validate_track_extension], null=True)
    episode_status = models.BooleanField(default=False)
    episode_release_date=models.DateTimeField()
    podcast_category_id = models.ForeignKey(PodcastCategory, default=0, related_name='episode', on_delete=models.DO_NOTHING)
    season_id = models.ForeignKey(Season, default=0, related_name='episodes', on_delete=models.DO_NOTHING)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.episode_title)