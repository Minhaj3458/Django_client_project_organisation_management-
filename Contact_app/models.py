from django.db import models

# Create your models here.

#Contact
class Contact(models.Model):
    full_name = models.CharField(max_length=60, blank=False,null=False)
    email = models.EmailField(max_length=60,blank=False,null=False)
    number = models.CharField(max_length=15, blank=False,null=False)
    subject = models.CharField(max_length=60, blank=False,null=True)
    message = models.CharField(max_length=100, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)