
from django.urls import path
from .import views
urlpatterns = [
    path('picture/',views.picture, name='picture'),
    path('documentation/',views.documentation, name='documentation'),

]
