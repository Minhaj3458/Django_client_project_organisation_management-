from django.shortcuts import render,redirect
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib import messages
from .import models,forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import  check_password
from django.contrib.auth.models import User


# Create your views here.
# manage users
def manage_user(request):
    show_user = models.UserProfile.objects.all().order_by('-id')
    context = {
        'show_user': show_user,
    }
    return render(request, 'Admin/page/manage_user.html',context)

# Add users
def add_user(request):
    if request.method == 'POST':
         password = request.POST.get('password')
         con_password = request.POST.get('confirm-password')
         cheack_email = request.POST.get('email')
         cheack_username = request.POST.get('username')
         if password == con_password:
             if models.UserProfile.objects.filter(username=cheack_username):
                 messages.warning(request, 'This UserName Already Exist')
                 return redirect('add_user')
             elif models.UserProfile.objects.filter(email= cheack_email):
                 messages.warning(request, 'This Email Already Exist')
                 return redirect('add_user')
             else:
                 mydata = models.UserProfile()
                 mydata.email = cheack_email
                 mydata.name = request.POST.get('name')
                 mydata.username = cheack_username
                 mydata.password = password
                 mydata.save()
                 messages.success(request, 'User Add Successfully!')
                 return redirect('add_user')
         else:
            messages.warning(request, "Password and confirm-password don't match")
            return redirect('add_user')

    return render(request, 'Admin/page/add_users.html')

# Delete users
def user_delete(request,Id):
    data = models.UserProfile.objects.get(id=Id)
    if data:
        data.delete()
        messages_delete = 'Data Delete Successfully!'
        messages.success(request, messages_delete)
        return redirect('manage_user')
    else:
        messages_delete = 'Something is Wrong!'
        messages.warning(request, messages_delete)
        return redirect('manage_user')
# Edit Users
def users_edit(request,Id):
    data = models.UserProfile.objects.get(id=Id)
    context = {
        'data': data,
    }

    if request.method == 'POST':
        data = forms.UserProfile_form(request.POST, request.FILES, instance=data)
        if data.is_valid():
            image = request.FILES.get('image')
            fname = image.name
            with open('static/Admin/images/user_pic/' + fname, 'wb+') as location:
                for ch in image.chunks():
                    location.write(ch)
            data.save()
            messages_update = 'Data Update Successfully!'
            messages.success(request,messages_update)
            return redirect('manage_user')
        else:
            messages_update = 'Something is Wrong!'
            messages.warning(request,messages_update)
            return redirect('manage_user')
    return render(request, 'Admin/page/users_update.html',context)

# user login
def mbss_login(request):
    if request.method == 'POST':
         username = request.POST['username']
         password_get = request.POST['password']
         user = models.UserProfile.objects.filter(username=username,password=password_get)
         if user:
             m = models.UserProfile.objects.get(username=request.POST['username'])
             request.session['user_id'] = m.id
             request.session['username'] = m.username
             return redirect('manage_user')
         else:
             messages.warning(request, 'Your username or password is invalid.')
             return redirect('mbss_login')
    return render(request, 'Admin/page/MBSS_login.html')

#user logout
def user_logout(request):
    logout(request)
    return redirect('mbss_login')

def forgot_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        password_get = request.POST['password']
        con_password = request.POST.get('confirm-password')
        if password_get == con_password:
            if models.UserProfile.objects.filter(username = username):
                models.UserProfile.objects.filter(username=username).update(password=password_get)
                messages_update = 'Password Update Successfully!'
                messages.success(request, messages_update)

            else:
                messages.warning(request, 'This UserName NOT Found')
                return redirect('forgot_password')

        else:
            messages.warning(request, "Password and confirm-password don't match")
            return redirect('forgot_password')

    return render(request, 'Admin/page/forgot_password.html')