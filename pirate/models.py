from django.db import models
from django.template.defaultfilters import slugify
import datetime
# models for media page


class Movie(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    content = models.TextField()
    slug = models.CharField(max_length=150, unique=True)
    date = models.DateField(auto_now_add=True)

    def save(self):
        super().save()
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%s' % (
            date.year, date.month, date.day, slugify(self.title)
        )
        super().save()


class Album(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    content = models.TextField()
    slug = models.CharField(max_length=150, unique=True)
    date = models.DateField(auto_now_add=True)

    def save(self):
        super().save()
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%s' % (
            date.year, date.month, date.day, slugify(self.title)
        )
        super().save()


# models for lifestyle page
class Gents(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    content = models.TextField()
    slug = models.CharField(max_length=150, unique=True)
    date = models.DateField(auto_now_add=True)

    def save(self):
        super().save()
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%s' % (
            date.year, date.month, date.day, slugify(self.title)
        )
        super().save()


class Ladies(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    content = models.TextField()
    slug = models.CharField(max_length=150, unique=True)
    date = models.DateField(auto_now_add=True)

    def save(self):
        super().save()
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%s' % (
            date.year, date.month, date.day, slugify(self.title)
        )
        super().save()


# models for technology
class Technology(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    content = models.TextField()
    slug = models.CharField(max_length=150, unique=True)
    date = models.DateField(auto_now_add=True)

    def save(self):
        super().save()
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%s' % (
            date.year, date.month, date.day, slugify(self.title)
        )
        super().save()
