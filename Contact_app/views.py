from django.shortcuts import render,redirect
from django.contrib import messages
from .import models
# Create your views here.
def contact(request):
    if request.method == 'POST':
        if request.method == 'POST':
            mydata = models.Contact()
            mydata.full_name = request.POST.get('full_name')
            mydata.email = request.POST.get('email')
            mydata.number = request.POST.get('number')
            mydata.subject = request.POST.get('subject')
            mydata.message = request.POST.get('message')
            mydata.save()
            messages.success(request, 'Message Send Successfully!')
            return redirect('contact')
        else:
            messages.warning(request, 'Message Not Send')
            return redirect('contact')
    return render(request, 'view/pages/contact.html')