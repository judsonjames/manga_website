from django.urls import path

from navigation.views import MainPage, MangaView, NewsView, AboutView

urlpatterns = [
    path('', MainPage.as_view()),
    path('news/', NewsView.as_view()),
    path('about/', AboutView.as_view()),
    path('manga/', MangaView.as_view()),
    path('manga/<str:title>/', MangaView.as_view()),
    path('manga/<str:title>/<int:chapter>/', MangaView.as_view()),
    path('manga/<str:title>/<int:chapter>/<int:page>', MangaView.as_view()),
]
