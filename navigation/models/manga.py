from django.db import models
from django.contrib.auth.models import User

class Manga(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    url_name = models.CharField(max_length=50, blank=False, null=False, default="?")
    cover = models.CharField(max_length=50, default="")
    author = models.ManyToManyField('Author')
    genres = models.ManyToManyField('Genre')
    tags = models.ManyToManyField('Tag')

    def __str__(self) -> str:
        return "{}".format(self.title)

class Genre(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
