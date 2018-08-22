from django.db import models
from django.contrib.auth.models import User

class Manga(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    genres = models.ManyToManyField('Genre')
    tags = models.ManyToManyField('Tag')

    def __str__(self) -> str:
        return "{}".format(self.name)

class Genre(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.title
