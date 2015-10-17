from django.db import models
import datetime
from django.template.defaultfilters import slugify
# Create your models here.


class Content(models.Model):
    content = models.TextField()
    slug = models.CharField(max_length=150, unique=True)
    date = models.DateField(auto_now_add=True)
    CATEGORY_CHOICE = (
        ('MOVIE', 'Movie'),
        ('SONG', 'Song'),
        ('LIFESTYLE', 'LifeStyle'),
        ('TECH', 'Technology')
    )
    slug = models.CharField(max_length=150, unique=True)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=10)

    def save(self):
        super().save()
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%s' % (
            date.year, date.month, date.day, slugify(self.title)
        )
        super().save()


class Latest(models.Model):
    reference = models.ForeignKey(Content)

    def save(self):
        if Latest.objects.counts() == 20:
            obj = Latest.objects.order_by('id').first()
            obj.delete()
        else:
            print("less than 20")
        super().save()
