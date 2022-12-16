
from django.urls import path
from .import views
urlpatterns = [
    path('news', views.news, name='news'),
    path('singleNews/<Id>', views.singleNews, name='singleNews'),
]
