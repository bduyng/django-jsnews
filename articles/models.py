from __future__ import unicode_literals

from django.utils import timezone
from django.db import models


# Create your models here.
class Article(models.Model):
    url = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    username = models.CharField(max_length=100)

    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    created_time = models.DateTimeField(editable=False)
    visited_time = models.DateTimeField(editable=False)
    bookmarked_time = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
            ''' On save, update timestamps '''
            if not self.id:
                self.created_time = timezone.now()
                return super(Article, self).save(*args, **kwargs)
