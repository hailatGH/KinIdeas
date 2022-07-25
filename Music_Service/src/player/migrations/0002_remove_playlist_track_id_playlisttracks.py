# Generated by Django 4.0.6 on 2022-07-25 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='track_id',
        ),
        migrations.CreateModel(
            name='PlayListTracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('playlist_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='playlist_n', to='player.playlist')),
                ('track_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='playlist_t', to='player.track')),
            ],
            options={
                'verbose_name': 'PlayList',
                'verbose_name_plural': 'PlayLists',
                'ordering': ['id'],
            },
        ),
    ]
