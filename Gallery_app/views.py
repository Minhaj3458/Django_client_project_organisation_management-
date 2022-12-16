from django.shortcuts import render
from Admin_app.models import Picture,Documentation
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

def picture(request):
    picture = Picture.objects.all().order_by('-id')
    picture_lat = Picture.objects.all().order_by('-id')[:4]
    paginator = Paginator(picture,1)  # Show 25 contacts per page

    page = request.GET.get('page')
    total = paginator.get_page(page)
    context = {
        'picture': total,
        'picture_lat': picture_lat,
    }
    return render(request, 'view/pages/picture.html',context)

def documentation(request):
    documentation1 = Documentation.objects.all().order_by('-id')
    paginator = Paginator(documentation1,1)  # Show 25 contacts per page
    documentation_lat = Documentation.objects.all().order_by('-id')[:1]
    page = request.GET.get('page')
    total = paginator.get_page(page)
    context = {
        'documentation1': total,
        'documentation_lat':documentation_lat,
    }
    return render(request,'view/pages/documentation.html',context)