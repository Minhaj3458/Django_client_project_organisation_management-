from django.shortcuts import render,redirect
from django.contrib import messages
from .import models
from Admin_app.models import Payment_system
# Create your views here.
def donate_Us(request):
        payment = Payment_system.objects.all().order_by('-id')
        context = {
            'payment': payment,
        }
        if request.method == 'POST':
            if request.method == 'POST':
                mydata = models.Donate()
                mydata.full_name = request.POST.get('full_name')
                mydata.email = request.POST.get('email')
                mydata.number= request.POST.get('number')
                mydata.bank_sl_tran = request.POST.get('bank_sl_tran')
                mydata.message = request.POST.get('message')
                mydata.save()
                messages.success(request, 'Message Send Successfully!')
                return redirect('donate_Us')
            else:
                messages.warning(request, 'Message Not Send')
                return redirect('donate_Us')

        return render(request, 'view/pages/donate_US.html',context)