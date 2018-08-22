from django.urls import path

from .views import MainPage

urlpatterns = [
  path('', MainPage.as_view()),
]
