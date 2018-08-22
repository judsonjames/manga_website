from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

class MainPage(View):
    def get(self, request: dict) -> HttpResponse:
        return HttpResponse("Main Page Goes Here")
    def post(self, request: dict) -> HttpResponse:
        return HttpResponse("Main Page Goes Here")