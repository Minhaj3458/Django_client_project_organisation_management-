from django.shortcuts import render
from Admin_app.models import News
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

def news(request):
    news = News.objects.all().order_by('-id')
    paginator = Paginator(news, 6)  # Show 25 contacts per page

    page = request.GET.get('page')
    total = paginator.get_page(page)
    context = {
        'news': total,
    }
    return render(request, 'view/pages/news.html',context)

def singleNews(request,Id):
    data = News.objects.get(id=Id)
    news = News.objects.all().order_by('-id')[:6]
    context = {
        'data': data,
        'news': news,
    }

    return render(request, 'view/pages/singleNews.html',context)