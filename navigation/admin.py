from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Manga)
admin.site.register(MangaChapter)
admin.site.register(MangaPage)
admin.site.register(Genre)
admin.site.register(Tag)
