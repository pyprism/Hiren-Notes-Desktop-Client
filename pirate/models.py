from django.db import models
# models for media page


class Movie(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)


class Album(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)


# models for lifestyle page
class Gents(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)


class Ladies(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)


# models for technology
class Technology(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)