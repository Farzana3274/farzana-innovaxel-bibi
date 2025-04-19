from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShortenURL.as_view()),
    path('shorten/<str:code>', views.RetrieveURL.as_view()),
   
]
