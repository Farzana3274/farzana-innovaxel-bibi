from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShortenURL.as_view()),
    path('shorten/<str:code>', views.RetrieveURL.as_view()),
    path('shorten/<str:code>/update', views.UpdateURL.as_view()),
    path('shorten/<str:code>/delete', views.DeleteURL.as_view()),
    path('shorten/<str:code>/stats', views.URLStats.as_view()),
   
]
