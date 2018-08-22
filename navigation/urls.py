from django.urls import path

from .views import MainPage
from .views import MangaView
# import .views.manga_view

urlpatterns = [
  path('', MainPage.as_view()),
  path('manga/', MangaView.ListManga),
  path('manga/<str:title>/', MangaView.ListChapters),
  path('manga/<str:title>/<int:chapter>/', MangaView.ListPages),
  path('manga/<str:title>/<int:chapter>/<int:page>', MangaView.ShowManga),
]
