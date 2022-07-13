from django.db import models
from core.settings import MEDIA_ROOT
from django.utils.translation import gettext_lazy as _
from core import validators

# Create your models here.

def banner_images(instance, filename):
    return '/'.join(['banner_images', str(instance.comapny_name), filename])
    # The directory arrangment will be [Media/banner_images/{filename}]

def logo_images(instance, filename):
    return '/'.join(['logo_images', str(instance.comapny_name), filename])
    # The directory arrangment will be [Media/logo_images/{filename}]

class CompanyProfile(models.Model):
    
    class Meta:
        verbose_name = _("CompanyProfile")
        verbose_name_plural = _("CompanyProfiles")
        ordering = ['id']
    
    comapny_name = models.CharField(max_length=100, default=_("Kin Ideas"), null=False, blank=False)
    contact_person = models.CharField(max_length=100, default=_("Pawlos Girma"), null=False, blank=False)
    address = models.CharField(max_length=100, default=_("22, Around Awraris Hotel, Teshab Building, 5th Floor"), null=False, blank=False)
    country = models.CharField(max_length=100, default=_("Ethiopia"), null=False, blank=False)
    city = models.CharField(max_length=100, default=_("Addis Ababa"), null=False, blank=False)
    state = models.CharField(max_length=100, default=_("Addis Ababa"), null=False, blank=False)
    postal_code = models.CharField(max_length=100, default=_("-"), null=False, blank=False)
    email = models.EmailField(max_length=100, default="admin@kinideas.com", null=False, blank=False)
    office_Phone_number = models.CharField(max_length=100, default=_("+251 XXX XXX XXX"), null=False, blank=False)
    mobile_Phone_number = models.CharField(max_length=100, default=_("+251 9XX XXX XXX"), null=False, blank=False)
    fax = models.CharField(max_length=100, default=_("+251 XXX XXX XXX"), null=False, blank=False)
    website = models.URLField(max_length=100, default="www.kinideas.com", null=False, blank=False)
    banner = models.ImageField(upload_to=banner_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=1023, null=False, blank=False)
    logo = models.ImageField(upload_to=logo_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=1023, null=False, blank=False)
    privecy = models.TextField(max_length=1023, blank=False, null=False)
    terms = models.TextField(max_length=1023, blank=False, null=False)
    help = models.TextField(max_length=1023, blank=False, null=False)
    about = models.TextField(max_length=1023, blank=False, null=False)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%d: %s' % (self.pk, self.comapny_name)