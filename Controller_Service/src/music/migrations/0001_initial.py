# Generated by Django 4.0.6 on 2022-07-22 07:05

import core.validators
from django.db import migrations, models
import django.db.models.deletion
import music.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(default='Collections', max_length=100)),
                ('album_cover', models.ImageField(max_length=1023, upload_to=music.models.albums_cover_images, validators=[core.validators.validate_image_extension])),
                ('album_description', models.TextField(blank=True, max_length=1023, null=True)),
                ('user_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(default='unknown', max_length=100)),
                ('artist_title', models.CharField(default='unknown', max_length=100)),
                ('artist_cover', models.ImageField(max_length=1023, upload_to=music.models.artists_cover_images, validators=[core.validators.validate_image_extension])),
                ('artist_description', models.TextField(blank=True, max_length=1023, null=True)),
                ('user_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_title', models.CharField(default='Other', max_length=100)),
                ('genre_cover', models.ImageField(max_length=1023, upload_to=music.models.genres_cover_images, validators=[core.validators.validate_image_extension])),
                ('genre_description', models.TextField(blank=True, max_length=1023, null=True)),
                ('user_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(default='Unknown_track', max_length=120)),
                ('track_description', models.TextField(blank=True, max_length=1023, null=True)),
                ('track_file', models.FileField(upload_to=music.models.track_files, validators=[core.validators.validate_track_extension])),
                ('track_status', models.BooleanField(default=False)),
                ('track_release_date', models.DateTimeField()),
                ('user_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('album_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tracks_al', to='music.album')),
                ('artist_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tracks_ar', to='music.artist')),
                ('genre_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tracks_g', to='music.genre')),
            ],
            options={
                'verbose_name': 'Track',
                'verbose_name_plural': 'Tracks',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Lyrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyrics_title', models.CharField(default='Other', max_length=100)),
                ('lyrics_detail', models.TextField(blank=True, null=True)),
                ('user_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('track_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lyrics', to='music.track')),
            ],
            options={
                'verbose_name': 'Lyrics',
                'verbose_name_plural': 'Lyrics',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artist_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, related_name='albums', to='music.artist'),
        ),
    ]
