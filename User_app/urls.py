
from django.urls import path
from .import views
urlpatterns = [
    path('manage_user', views.manage_user, name='manage_user'),
    path('add_user', views.add_user, name='add_user'),
    path('user_delete/<Id>', views.user_delete, name='user_delete'),
    path('users_edit/<Id>', views.users_edit, name='users_edit'),
    path('mbss_login', views.mbss_login, name='mbss_login'),
    path('logout', views.user_logout, name='logout'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
]
