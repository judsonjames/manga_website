from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from navigation.models import NewsPost

class NewsView(View):
    def get(self, request:dict) -> HttpResponse:
        posts = NewsPost.objects.all().order_by('-date')
        return render(request, 'home/news_section.html', {'posts':posts})
    def post(self, request:dict) -> HttpResponse:
        return HttpResponse("POST NEWS VIEW")
