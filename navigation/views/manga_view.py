from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from navigation.models import Manga, MangaChapter, MangaPage

class MangaView(View):

    def ListManga(self, request=HttpRequest()) -> HttpResponse:
        manga = Manga.objects.all()
        return render(request, 'manga/manga_list.html', {'manga':manga})

    def ListChapters(self, title:str, request=HttpRequest()) -> HttpResponse:
        manga = Manga.objects.get(url_name=title)
        chapters = MangaChapter.objects.filter(manga=manga).order_by('order')
        return render(request, 'manga/chapter_list.html', {'chapters':chapters, 'title':title})

    def ListPages(self, title:str, chapter:int, request=HttpRequest()) -> HttpResponse:
        manga = Manga.objects.get(url_name=title)
        chap = MangaChapter.objects.get(manga=manga, order=chapter)
        pages = MangaPage.objects.filter(chapter=chap).order_by('order')
        return render(request, 'manga/page_list.html', {'pages':pages, 'title':title, 'chapter':chap.order})

    def ShowManga(self, title:str, chapter:int, page:int, request=HttpRequest()) -> HttpResponse:
        manga = Manga.objects.get(url_name=title)
        chap = MangaChapter.objects.get(manga=manga)
        page = MangaPage.objects.get(chapter=chap, order=page)
        return render(request, 'manga/show_manga.html',
                { 'page':page })
        # return HttpResponse('Show Manga')
