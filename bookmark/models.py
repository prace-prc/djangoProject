from django.db import models


# Create your models here.
class Bookmark(models.model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)

    def __str__(self):
        return self.title
