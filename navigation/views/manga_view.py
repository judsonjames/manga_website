from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

class MangaView(View):
    def get(self, request: dict) -> HttpResponse:
        page = request.GET.get('page', None)
        if page == 'sample':
            print('Thing')
            return render(request, 'sample/sample.html', {})
        else:
            return HttpResponse("Manga Page Goes Here")
    def post(self, request: dict) -> HttpResponse:
        return HttpResponse("Manga Page Goes Here")

    def __ListManga(self, request: dict) -> HttpResponse:
        pass
    def __ListChapters(self, request: dict) -> HttpResponse:
        pass
    def __ListPages(self, request: dict) -> HttpResponse:
        pass
