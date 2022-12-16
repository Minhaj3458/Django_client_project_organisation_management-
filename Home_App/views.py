from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from Admin_app.models import Personal_Info,Picture,News
from django.db.models.functions import Length
# Create your views here.

def index(request):
    picture = Picture.objects.all().order_by('-id')[:9]
    picture_title = Picture.objects.all().order_by('-id')[:1]
    news = News.objects.all().order_by('-id')[:3]
    news_title = News.objects.all().order_by('-id')[:1]
    context = {
        'picture': picture,
        'picture_title': picture_title,
        'news': news,
        'news_title': news_title,
    }
    return render(request,'view/index.html',context)


def about(request):
    return render(request, 'view/pages/about.html')
