from django.shortcuts import render
from Admin_app.models import Documents
# Create your views here.
def documents(request):
    docum = Documents.objects.all().order_by('-id')[:5]
    context = {
        'docum': docum,
    }
    return render(request, 'view/pages/documents.html',context)