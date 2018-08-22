from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

class MangaView(View):
    def get(self, request: dict) -> HttpResponse:
        return HttpResponse("Manga Page Goes Here")
    def post(self, request: dict) -> HttpResponse:
        return HttpResponse("Manga Page Goes Here")
