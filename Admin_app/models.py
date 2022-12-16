from django.db import models

# Create your models here.

# Personal Information
class Personal_Info(models.Model):
    email = models.EmailField(max_length=100,blank=True,)
    phone1 = models.CharField(max_length=15,blank=True,null=True)
    phone2 = models.CharField( max_length=15, blank=True, null=True)
    address = models.TextField( max_length=100, blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)

# Social Media
class Social_Media(models.Model):
    facebook = models.CharField(max_length=60,blank=True,)
    twitter  = models.CharField(max_length=60,blank=True,null=True)
    instagram = models.CharField( max_length=60, blank=True, null=True)
    linkedin = models.TextField( max_length=60, blank=True, null=True)
    dribbble = models.TextField(max_length=60, blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)


# Picture
class Picture(models.Model):
    title = models.CharField(max_length=70,blank=True,)
    image = models.ImageField(upload_to='static/view/assets/img/Gallery/picture/',max_length=100, blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)


#Documentation

class Documentation(models.Model):
    image1 = models.ImageField(upload_to='static/view/assets/img/Gallery/document/',max_length=100, blank=True, null=True)
    image2 = models.ImageField(upload_to='static/view/assets/img/Gallery/document/', max_length=100, blank=True, null=True)
    image3 = models.ImageField(upload_to='static/view/assets/img/Gallery/document/', max_length=100, blank=True,null=True)
    date_time = models.DateTimeField(auto_now_add=True)

#News
class News(models.Model):
    title    = models.CharField(max_length=70,blank=True,)
    news_title  = models.CharField(max_length=40,blank=True,null=True)
    news_message = models.CharField( max_length=1200, blank=True, null=True)
    s_image = models.ImageField(upload_to='static/view/assets/img/News_Picture/', max_length=100, blank=False, null=True)
    l_image1 = models.ImageField(upload_to='static/view/assets/img/News_Picture/', max_length=100, blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)

#Documents
class Documents(models.Model):
    doc_title = models.CharField(max_length=35, blank=True,null=True)
    doc_pdf = models.FileField(upload_to='static/view/assets/img/statement_pdf/',blank=True,null=True)
    date_time = models.DateTimeField(auto_now_add=True)

#Donate Payment System
class Payment_system(models.Model):
     bankName = models.CharField(max_length=60, blank=False,null=True)
     ac_no = models.CharField(max_length=25, blank=False, null=True)
     branch = models.CharField(max_length=100, blank=False, null=True)
     bkash_acc_name = models.CharField(max_length=60, blank=False, null=True)
     bkash_acc_number = models.CharField(max_length=25, blank=False, null=True)
     bkash_acc_address = models.CharField(max_length=100, blank=False, null=True)
     nagad_acc_name = models.CharField(max_length=60, blank=False, null=True)
     nagad_acc_number = models.CharField(max_length=25, blank=False, null=True)
     nagad_acc_address = models.CharField(max_length=100, blank=False, null=True)
     date_time = models.DateTimeField(auto_now_add=True)





