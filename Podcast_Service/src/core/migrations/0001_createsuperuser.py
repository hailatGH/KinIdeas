import os

from django.contrib.auth.models import User
from django.db import migrations


def createsuperuser(apps, schema_editor):
    podcast_admin_password = os.environ["PODCAST_ADMIN_PASSWORD"] 
    User.objects.create_superuser("admin", password=podcast_admin_password)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunPython(createsuperuser)
    ]