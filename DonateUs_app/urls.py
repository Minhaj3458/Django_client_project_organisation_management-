
from django.urls import path
from .import views
urlpatterns = [
    path('donate_Us/',views.donate_Us, name='donate_Us'),

]
