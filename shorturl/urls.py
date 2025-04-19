from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShortenURL.as_view()),
   
]
