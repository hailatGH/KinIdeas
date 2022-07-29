import os

from django.contrib.auth.models import User
from django.db import migrations


def createsuperuser(apps, schema_editor):
    radio_admin_password = os.environ["RADIO_ADMIN_PASSWORD"] 
    User.objects.create_superuser("admin", password=radio_admin_password)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunPython(createsuperuser)
    ]