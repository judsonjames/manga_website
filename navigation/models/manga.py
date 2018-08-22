from django.db import models

class Manga(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    genres = models.ManyToManyField('Genre')
    tags = models.ManyToManyField('Tag')

    def __str__(self) -> str:
        return ""

class Genre(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.title
