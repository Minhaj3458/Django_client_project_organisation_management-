from django.db import models

# Create your models here.
#Donate_Us
class Donate(models.Model):
    full_name = models.CharField(max_length=60, blank=False,)
    email = models.EmailField(max_length=60,blank=False,)
    number = models.CharField(max_length=15, blank=False,)
    bank_sl_tran = models.CharField(max_length=60, blank=False,null=True)
    message = models.CharField(max_length=100, blank=True,)
    date_time = models.DateTimeField(auto_now_add=True)