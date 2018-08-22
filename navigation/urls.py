from django.urls import path

from .views import MainPage
from .views import MangaView

urlpatterns = [
  path('', MainPage.as_view()),
  path('manga/<str:manga_name>/<int:manga_page>/', MangaView.as_view()),
]
