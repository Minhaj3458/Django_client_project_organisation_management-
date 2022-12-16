from django.shortcuts import render,redirect
from django.contrib import messages
from DonateUs_app.models import Donate
from DonateUs_app.forms import donate_form
from Contact_app.models import Contact
from django.contrib.auth.decorators import login_required
from .import models,forms
import os
# Create your views here.
def index(request):
    return render(request, 'Admin/index.html')

# Personal Information Add
def add_info(request):
    if request.method == 'POST':
        if request.method == 'POST':
            mydata = models.Personal_Info()
            mydata.email = request.POST.get('email')
            mydata.phone1 = request.POST.get('phone1')
            mydata.phone2 = request.POST.get('phone2')
            mydata.address = request.POST.get('address')
            mydata.save()

            messages.success(request,'Data Save Successfully!')
            return render(request, 'Admin/page/add_personal_info.html')
        else:
             messages.warning(request, 'Data Not Save')
             return render(request, 'Admin/page/add_personal_info.html')

    return render(request, 'Admin/page/add_personal_info.html')



# Personal Information Manage
def manage_info(request):
    personal = models.Personal_Info.objects.all().order_by('-id')
    context = {
        'personal': personal,
    }
    return render(request, 'Admin/page/manage_info.html',context)

# Personal Information delete
def info_delete(request,Id):
    data = models.Personal_Info.objects.get(id=Id)
    if data:
        data.delete()
        messages_delete = 'Data Delete Successfully!'
        messages.success(request, messages_delete)
        return redirect('manage_info')
    else:
        messages_delete = 'Something is Wrong!'
        messages.warning(request, messages_delete)
        return redirect('manage_info')

# Personal Information Edit
def info_edit(request,Id):
    data = models.Personal_Info.objects.get(id=Id)
    if request.method == 'POST':
        data = forms.Personal_Info_form(request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            messages_update = 'Data Update Successfully!'
            messages.success(request,messages_update)
            return redirect('manage_info')
        else:
            messages_update = 'Something is Wrong!'
            messages.warning(request,messages_update)
            return redirect('manage_info')
    return render(request, 'Admin/page/personal_info_edit.html',{'data':data})

# add social media

def add_media(request):
    if request.method == 'POST':
        if request.method == 'POST':
            mydata = models.Social_Media()
            mydata.facebook = request.POST.get('facebook')
            mydata.twitter = request.POST.get('twitter')
            mydata.instagram= request.POST.get('instagram')
            mydata.linkedin = request.POST.get('linkedin')
            mydata.dribbble = request.POST.get('dribbble')
            mydata.save()
            messages.success(request, 'Data Save Successfully!')
            return redirect('add_media')
        else:
            messages.warning(request, 'Data Not Save')
            return redirect('add_media')
    return render(request, 'Admin/page/add_social_media.html')

# add social media
def manage_media(request):
    media = models.Social_Media.objects.all().order_by('-id')
    context = {
        'media': media,
    }
    return render(request, 'Admin/page/manage_social_media.html',context)

# social media delete
def media_delete(request,Id):
    data = models.Social_Media.objects.get(id=Id)
    if data:
        data.delete()
        messages_delete = 'Data Delete Successfully!'
        messages.success(request, messages_delete)
        return redirect('manage_media')
    else:
        messages_delete = 'Something is Wrong!'
        messages.warning(request, messages_delete)
        return redirect('manage_media')

#  social media Edit
def media_edit(request,Id):
    data = models.Social_Media.objects.get(id=Id)
    if request.method == 'POST':
        data = forms.social_media_form(request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            messages_update = 'Data Update Successfully!'
            messages.success(request,messages_update)
            return redirect('manage_media')
        else:
            messages_update = 'Something is Wrong!'
            messages.warning(request,messages_update)
            return redirect('manage_media')
    return render(request, 'Admin/page/edit_media.html',{'data':data})

# add Picture

def add_picture(request):
    if request.method == 'POST':
        upload_image = request.FILES.get('image')
        # fname = upload_image.name
        # with open(fname, 'wb+') as location:
        #     for ch in upload_image.chunks():
        #         location.write(ch)
        if request.method == 'POST':
            mydata = models.Picture()
            mydata.title = request.POST.get('title')
            mydata.image = upload_image
            mydata.save()
            messages.success(request,'Picture Save Successfully!')
            return redirect('add_picture')
        else:
            messages.warning(request,'Picture Not Save')
            return redirect('add_picture')
    return render(request, 'Admin/page/add_picture.html')

# manage Picture
def manage_picture(request):
    picture = models.Picture.objects.all().order_by('-id')
    context = {
        'picture':  picture,
    }
    return render(request, 'Admin/page/manage_picture.html',context)


# Picture delete
def picture_delete(request,Id):
    data = models.Picture.objects.get(id=Id)
    if data:
        if len(data.image) > 0:
            os.remove(data.image.path)
        data.delete()
        messages_delete = 'Data Delete Successfully!'
        messages.success(request, messages_delete)
        return redirect('manage_picture')
    else:
        messages_delete = 'Something is Wrong!'
        messages.warning(request, messages_delete)
        return redirect('manage_picture')


#  Picture Edit
def picture_edit(request,Id):
    data = models.Picture.objects.get(id=Id)
    if request.method == 'POST':
        data = forms.picture_form(request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            messages_update = 'Data Update Successfully!'
            messages.success(request, messages_update)
            return redirect('manage_picture')
        else:
            messages_update = 'Something is Wrong!'
            messages.warning(request, messages_update)
            return redirect('manage_picture')
    return render(request, 'Admin/page/edit_picture.html',{'data':data})

# Add Documentation
def add_documentation(request):
    if request.method == 'POST':
        upload_image1 = request.FILES.get('image1')
        # fname = upload_image1.name
        # with open(fname, 'wb+') as location:
        #     for ch in upload_image1.chunks():
        #         location.write(ch)
        upload_image2 = request.FILES.get('image2')
        # fname = upload_image2.name
        # with open(fname, 'wb+') as location:
        #     for ch in upload_image2.chunks():
        #         location.write(ch)
        upload_image3 = request.FILES.get('image3')
        # fname = upload_image3.name
        # with open(fname, 'wb+') as location:
        #     for ch in upload_image3.chunks():
        #         location.write(ch)
        if request.method == 'POST':
            mydata = models.Documentation()
            mydata.image1 = upload_image1
            mydata.image2 = upload_image2
            mydata.image3 = upload_image3
            mydata.save()
            messages.success(request,'Documentation Save Successfully!')
            return redirect('add_documentation')
        else:
            messages.warning(request,'Documentation Not Save')
            return redirect('add_documentation')
    return render(request, 'Admin/page/add_documentation.html')

# Manage Documentation
def manage_documentation(request):
    documentation = models.Documentation.objects.all().order_by('-id')
    context = {
        'documentation': documentation,
    }
    return render(request, 'Admin/page/manage_documentation.html',context)

# Documentation delete
def documentation_delete(request,Id):
    data = models.Documentation.objects.get(id=Id)
    if data:
        if len(data.image1) > 0:
            os.remove(data.image1.path)
        if len(data.image2) > 0:
            os.remove(data.image2.path)
        if len(data.image3) > 0:
            os.remove(data.image3.path)
        data.delete()
        messages_delete = 'Data Delete Successfully!'
        messages.success(request, messages_delete)
        return redirect('manage_documentation')
    else:
        messages_delete = 'Something is Wrong!'
        messages.warning(request, messages_delete)
        return redirect('manage_documentation')

#  Documentation Edit
def documentation_edit(request,Id):
    data = models.Documentation.objects.get(id=Id)
    if request.method == 'POST':
        data = forms.documentation_form(request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            messages_update = 'Data Update Successfully!'
            messages.success(request, messages_update)
            return redirect('manage_documentation')
        else:
            messages_update = 'Something is Wrong!'
            messages.warning(request, messages_update)
            return redirect('manage_documentation')
    return render(request, 'Admin/page/documentation_update.html',{'data':data})

# Add News
def add_news(request):
    if request.method == 'POST':
        upload_image1 = request.FILES.get('s_image')
        # fname = upload_image1.name
        # with open(fname, 'wb+') as location:
        #     for ch in upload_image1.chunks():
        #         location.write(ch)
        upload_image2 = request.FILES.get('l_image1')
        # fname = upload_image2.name
        # with open(fname, 'wb+') as location:
        #     for ch in upload_image2.chunks():
        #         location.write(ch)
        if request.method == 'POST':
            mydata = models.News()
            mydata.title = request.POST.get('title')
            mydata.news_title = request.POST.get('news_title')
            mydata.s_image = upload_image1
            mydata.l_image1 = upload_image2
            mydata.news_message = request.POST.get('news_message')
            mydata.save()
            messages.success(request, 'News Save Successfully!')
            return redirect('add_news')
        else:
            messages.warning(request, 'News Not Save')
            return redirect('add_news')

    return render(request,'Admin/page/add_news.html')

#Manage News
def manage_news(request):
    news = models.News.objects.all().order_by('-id')
    context = {
        'news': news,
    }
    return render(request, 'Admin/page/manage_news.html',context)


# News delete
def news_delete(request,Id):
    data = models.News.objects.get(id=Id)
    if data:
        if len(data.s_image) > 0:
            os.remove(data.s_image.path)
        if len(data.l_image1) > 0:
            os.remove(data.l_image1.path)
        data.delete()
        messages_delete = 'Data Delete Successfully!'
        messages.success(request, messages_delete)
        return redirect('manage_news')
    else:
        messages_delete = 'Something is Wrong!'
        messages.warning(request, messages_delete)
        return redirect('manage_news')


#  News Edit
def news_edit(request,Id):
    data = models.News.objects.get(id=Id)
    if request.method == 'POST':
        data = forms.news_form(request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            messages_update = 'Data Update Successfully!'
            messages.success(request, messages_update)
            return redirect('manage_news')
        else:
            messages_update = 'Something is Wrong!'
            messages.warning(request, messages_update)
            return redirect('manage_news')
    return render(request, 'Admin/page/news_update.html',{'data':data})

# Add Documents
def add_documents(request):
    if request.method == 'POST':
        upload_image1 = request.FILES.get('doc_pdf')
        # fname = upload_image1.name
        # with open(fname, 'wb+') as location:
        #     for ch in upload_image1.chunks():
        #         location.write(ch)
        if request.method == 'POST':
            mydata = models.Documents()
            mydata.doc_title = request.POST.get('doc_title')
            mydata.doc_pdf = upload_image1
            mydata.save()
            messages.success(request, 'Documents Save Successfully!')
            return redirect('add_documents')
        else:
            messages.warning(request, 'Documents Not Save')
            return redirect('add_documents')
    return render(request, 'Admin/page/add_Documents.html')

# Manage Documents
def manage_documents(request):
    documents = models.Documents.objects.all().order_by('-id')
    context = {
        'documents': documents,
    }
    return render(request, 'Admin/page/manage_documents.html',context)

 # Delete Documents
def documents_delete(request,Id):
    data = models.Documents.objects.get(id=Id)
    if data:
        if len(data.doc_pdf) > 0:
            os.remove(data.doc_pdf.path)
        data.delete()
        messages_delete = 'Data Delete Successfully!'
        messages.success(request, messages_delete)
        return redirect('manage_documents')
    else:
        messages_delete = 'Something is Wrong!'
        messages.warning(request, messages_delete)
        return redirect('manage_documents')


 # Edit Documents
def documents_edit(request,Id):
    data = models.Documents.objects.get(id=Id)
    if request.method == 'POST':
        data = forms.documents_form(request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            messages_update = 'Data Update Successfully!'
            messages.success(request, messages_update)
            return redirect('manage_documents')
        else:
            messages_update = 'Something is Wrong!'
            messages.warning(request, messages_update)
            return redirect('manage_documents')
    return render(request, 'Admin/page/documents_update.html',{'data':data})

# Manage Donate_Us
def manage_donate_us(request):
    donate = Donate.objects.all().order_by('-id')
    context = {
        'donate': donate,
    }
    return render(request, 'Admin/page/manage_donateUs.html',context)

# Delete Donate_Us
def donate_delete(request,Id):
    data = Donate.objects.get(id=Id)
    if data:
        data.delete()
        messages_delete = 'Data Delete Successfully!'
        messages.success(request, messages_delete)
        return redirect('manage_donate_us')
    else:
        messages_delete = 'Something is Wrong!'
        messages.warning(request, messages_delete)
        return redirect('manage_donate_us')

# Edit Donate Us
def donate_edit(request,Id):
    data = Donate.objects.get(id=Id)
    if request.method == 'POST':
        data = donate_form(request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            messages_update = 'Data Update Successfully!'
            messages.success(request, messages_update)
            return redirect('manage_donate_us')
        else:
            messages_update = 'Something is Wrong!'
            messages.warning(request, messages_update)
            return redirect('manage_donate_us')
    return render(request, 'Admin/page/donate_update.html',{'data':data})


# Add Donate Payment System
def add_payment_system(request):
    if request.method == 'POST':
        if request.method == 'POST':
            mydata = models.Payment_system()
            mydata.bankName = request.POST.get('bankName')
            mydata.ac_no = request.POST.get('ac_no')
            mydata.branch = request.POST.get('branch')
            mydata.bkash_acc_name = request.POST.get('bkash_acc_name')
            mydata.bkash_acc_number = request.POST.get('bkash_acc_number')
            mydata.bkash_acc_address = request.POST.get('bkash_acc_address')
            mydata.nagad_acc_name = request.POST.get('nagad_acc_name')
            mydata.nagad_acc_number = request.POST.get('nagad_acc_number')
            mydata.nagad_acc_address= request.POST.get('nagad_acc_address')
            mydata.save()
            messages.success(request, 'Data Save Successfully!')
            return redirect('add_payment_system')
        else:
            messages.warning(request, 'Data Not Save')
            return redirect('add_payment_system')
    return render(request, 'Admin/page/add_payment_system.html')


# Manage Donate payment System
def manage_payment(request):
    payment = models.Payment_system.objects.all().order_by('-id')
    context = {
        'payment': payment,
    }
    return render(request, 'Admin/page/manage_payment.html',context)


# Delete Donate payment System
def payment_delete(request,Id):
    data = models.Payment_system.objects.get(id=Id)
    if data:
        data.delete()
        messages_delete = 'Data Delete Successfully!'
        messages.success(request, messages_delete)
        return redirect('manage_payment')
    else:
        messages_delete = 'Something is Wrong!'
        messages.warning(request, messages_delete)
        return redirect('manage_payment')


# Edit Donate payment System
def payment_edit(request,Id):
    data = models.Payment_system.objects.get(id=Id)
    if request.method == 'POST':
        data = forms.payment_form(request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            messages_update = 'Data Update Successfully!'
            messages.success(request, messages_update)
            return redirect('manage_payment')
        else:
            messages_update = 'Something is Wrong!'
            messages.warning(request, messages_update)
            return redirect('manage_payment')
    return render(request, 'Admin/page/payment_update.html',{'data':data})


# Manage Contact
def manage_contact(request):
    contact = Contact.objects.all().order_by('-id')
    context = {
        'contact': contact,
    }
    return render(request, 'Admin/page/manage_contact.html',context)


# Delete Contact
def contact_delete(request,Id):
    data =Contact.objects.get(id=Id)
    if data:
        data.delete()
        messages_delete = 'Data Delete Successfully!'
        messages.success(request, messages_delete)
        return redirect('manage_contact')
    else:
        messages_delete = 'Something is Wrong!'
        messages.warning(request, messages_delete)
        return redirect('manage_contact')


# Edit Contact
def contact_edit(request,Id):
    data = Contact.objects.get(id=Id)
    if request.method == 'POST':
        data = forms.contact_form(request.POST, request.FILES, instance=data)
        if data.is_valid():
            data.save()
            messages_update = 'Data Update Successfully!'
            messages.success(request, messages_update)
            return redirect('manage_contact')
        else:
            messages_update = 'Something is Wrong!'
            messages.warning(request, messages_update)
            return redirect('manage_contact')
    return render(request, 'Admin/page/contact_update.html',{'data':data})

