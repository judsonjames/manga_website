from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

class AboutView(View):
    def get(self, request:dict) -> HttpResponse:
        return render(request, 'home/about.html', {})
    def post(self, request:dict) -> HttpResponse:
        return HttpResponse("POST ABOUT VIEW")
