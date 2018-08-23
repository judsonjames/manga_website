from django.db import models

class NewsPost(models.Model):
    title = models.CharField(max_length=50, default="Title")
    post = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.date, self.title)
