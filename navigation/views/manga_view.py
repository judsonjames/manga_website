from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

class MangaView(View):

    def ListManga(self) -> HttpResponse:
        return HttpResponse('List all Manga on this page')

    def ListChapters(self, title: str) -> HttpResponse:
        return HttpResponse('List Chapters for Manga: \'{}\''.format(title))

    def ListPages(self, title: str, chapter: int) -> HttpResponse:
        return HttpResponse('List Pages for {}, Chapter: \'{}\''.format(title, chapter))

    def ShowManga(self, title: str, chapter: int, page: int) -> HttpResponse:
        return HttpResponse('Show Manga')
