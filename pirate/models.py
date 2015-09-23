from django.db import models
from ckeditor.fields import RichTextField
# models for media page


class Movie(models.Model):
    title = models.CharField(max_length=2000)
    name = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField(null=True, blank=True)


class Url(models.Model):
    movie_id = models.ForeignKey(Movie)
    url = models.URLField(max_length=2000)


class Album(models.Model):
    album_title = models.CharField(max_length=400, null=False, blank=False)


class Tracks(models.Model):
    album_id = models.ForeignKey(Album)
    track_name = models.CharField(max_length=200, null=False, blank=False)
    track_url = models.URLField(max_length=2000)


# models for lifestyle page
class Gents(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    content = RichTextField()


class Ladies(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    content = RichTextField()


# models for technology
class Technology(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    content = RichTextField()
