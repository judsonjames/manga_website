from django.urls import path

from .views import MainPage
from .views import MangaView
# import .views.manga_view

urlpatterns = [
  path('', MainPage.as_view()),
  path('manga/', MangaView.as_view()),
  path('manga/<str:title>/', MangaView.as_view()),
  path('manga/<str:title>/<int:chapter>/', MangaView.as_view()),
  path('manga/<str:title>/<int:chapter>/<int:page>', MangaView.as_view()),
]
