from django.db import models
from django.core.validators import MaxValueValidator as Max, MinValueValidator as Min

class MangaChapter(models.Model):
    manga = models.ForeignKey('Manga', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=False, default="")
    order = models.IntegerField(default=1, validators=[Min(1), Max(999)])


    def __str__(self) -> str:
        return "{}, {}".format(self.manga.title, self.title)
