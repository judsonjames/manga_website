from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from navigation.models import Manga, MangaChapter, MangaPage
from django.core.exceptions import ObjectDoesNotExist

class MangaView(View):

    def get(self, request:dict, **kwargs:dict) -> HttpResponse:
        """ GET
        """
        title = self.kwargs.get('title', 'no_title')
        chapter = self.kwargs.get('chapter', '0')
        page = self.kwargs.get('page', '0')
        if title == 'no_title':
            return self.__ListManga(request)
        elif chapter == '0':
            return self.__ListChapters(request)
        elif page == '0':
            return self.__ListPages(request)
        else:
            return self.__ShowManga(request)

    def post(self, request:dict) -> HttpResponse:
        """ POST
        This should not be accessible quite yet
        """
        return HttpResponse("POST")

    def __ListManga(self, request:dict, **kwargs:dict) -> HttpResponse:
        """ List Manga
        Returns a list of all Manga that are in the system
        """
        manga = Manga.objects.all()
        return render(request, 'manga/manga_list.html', {'manga':manga})

    def __ListChapters(self, request:dict, **kwargs:dict) -> HttpResponse:
        """ List Chapters
        Returns a list of the chapters to the Manga

        Raises:
            1) Manga.DoesNotExist if the manga does not exist
        """
        title = self.kwargs.get('title', 'no_title')
        manga = None
        try:
            manga = Manga.objects.get(url_name=title)
        except Manga.DoesNotExist:
            return redirect('/manga')
        chapters = MangaChapter.objects.filter(manga=manga).order_by('order')
        return render(request, 'manga/chapter_list.html', {'chapters':chapters, 'title':title})

    def __ListPages(self, request:dict, **kwargs:dict) -> HttpResponse:
        """ List Pages
        Returns a list of the page to the Chapter

        Raises:
            1) Manga.DoesNotExist if the manga does not exist
            2) MangaChapter.DoesNotExist if the chapter does not exist
        """
        title = self.kwargs.get('title', 'no_title')
        chapter_num = self.kwargs.get('chapter', '0')

        manga = None
        chapter = None
        try:
            manga = Manga.objects.get(url_name=title)
            chapter = MangaChapter.objects.get(manga=manga, order=chapter_num)
        except Manga.DoesNotExist:
            return redirect('/manga')
        except MangaChapter.DoesNotExist:
            return redirect('/manga/{}'.format(title))
        pages = MangaPage.objects.filter(chapter=chapter).order_by('order')
        return render(request, 'manga/page_list.html',
                {'pages':pages, 'title':title, 'chapter':chapter.order})

    def __ShowManga(self, request:dict, **kwargs:dict) -> HttpResponse:
        """ Show Manga
        Returns a page with the image

        Raises:
            1) Manga.DoesNotExist if the manga does not exist
            2) MangaChapter.DoesNotExist if the chapter does not exist
            3) MangaPage.DoesNotExist if the page does not exist
        """
        title = self.kwargs.get('title', 'no_title')
        chapter_num = self.kwargs.get('chapter', '0')
        page_num = self.kwargs.get('page', '0')

        manga = None
        chapter = None
        page = None
        try:
            manga = Manga.objects.get(url_name=title)
            chapter = MangaChapter.objects.get(manga=manga, order=chapter_num)
            page = MangaPage.objects.get(chapter=chapter_num, order=page_num)
        except Manga.DoesNotExist:
            return redirect('/manga')
        except MangaChapter.DoesNotExist:
            return redirect('/manga/{}'.format(title))
        except MangaPage.DoesNotExist:
            return redirect('/manga/{}/{}'.format(title, chapter_num))

        # Constructs the context for the Template
        context = {'page':page, 'title':title, 'chapter':chapter_num,
                'next':(page.order+1), 'prev':(page.order-1)}

        # Checks to see if we can go to next page
        if int(page_num) >= chapter.pages.count():
            context.update({'last_chapter':True})
        else:
            context.update({'last_chapter':False})

        # Checks to see if we can go to last page
        if int(page_num) <= 1:
            context.update({'first_chapter':True})
        else:
            context.update({'first_chapter':False})

        return render(request, 'manga/show_manga.html', context)
