
from django.urls import path
from .import views

urlpatterns = [
    path('index',views.index, name='index'),
    # Personal Information
    path('add_info',views.add_info, name='add_info'),
    path('manage_info',views.manage_info, name='manage_info'),
    path('info_delete/<Id>', views.info_delete, name='info_delete'),
    path('info_edit/<Id>', views.info_edit, name='info_edit'),
    # Social Media
    path('add_media', views.add_media, name='add_media'),
    path('manage_media', views.manage_media, name='manage_media'),
    path('media_delete/<Id>', views.media_delete, name='media_delete'),
    path('media_edit/<Id>', views.media_edit, name='media_edit'),

    # Picture
    path('add_picture', views.add_picture, name='add_picture'),
    path('manage_picture', views.manage_picture, name='manage_picture'),
    path('picture_delete/<Id>', views.picture_delete, name='picture_delete'),
    path('picture_edit/<Id>', views.picture_edit, name='picture_edit'),

    # Documentation
    path('add_documentation', views.add_documentation, name='add_documentation'),
    path('manage_documentation', views.manage_documentation, name='manage_documentation'),
    path('documentation_delete/<Id>', views.documentation_delete, name='documentation_delete'),
    path('documentation_edit/<Id>', views.documentation_edit, name='documentation_edit'),

    # News
    path('add_news', views.add_news, name='add_news'),
    path('manage_news', views.manage_news, name='manage_news'),
    path('news_delete/<Id>', views.news_delete, name='news_delete'),
    path('news_edit/<Id>', views.news_edit, name='news_edit'),

   # Documents
    path('add_documents', views.add_documents, name='add_documents'),
    path('manage_documents', views.manage_documents, name='manage_documents'),
    path('documents_delete/<Id>', views.documents_delete, name='documents_delete'),
    path('documents_edit/<Id>', views.documents_edit, name='documents_edit'),

   # Donate_us
    path('manage_donate_us', views.manage_donate_us, name='manage_donate_us'),
    path('donate_delete/<Id>', views.donate_delete, name='donate_delete'),
    path('donate_edit/<Id>', views.donate_edit, name='donate_edit'),

    # Donate Payment System
    path('add_payment_system', views.add_payment_system, name='add_payment_system'),
    path('manage_payment', views.manage_payment, name='manage_payment'),
    path('payment_delete/<Id>', views.payment_delete, name='payment_delete'),
    path('payment_edit/<Id>', views.payment_edit, name='payment_edit'),

   # Contact
    path('manage_contact', views.manage_contact, name='manage_contact'),
    path('contact_delete/<Id>', views.contact_delete, name='contact_delete'),
    path('contact_edit/<Id>', views.contact_edit, name='contact_edit'),

]
