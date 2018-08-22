from django.db import models
from django.core.validators import MaxValueValidator as Max, MinValueValidator as Min

class MangaPage(models.Model):
    chapter = models.ForeignKey('MangaChapter', on_delete=models.CASCADE, related_name='pages')
    order = models.IntegerField(default=1, validators=[Min(1), Max(999)])
    image_link = models.CharField(max_length=100, blank=False, null=False, default="")


    def __str__(self) -> str:
        return "Page {}, {}".format(self.order, self.chapter)
