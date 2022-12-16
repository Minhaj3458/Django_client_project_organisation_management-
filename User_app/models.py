from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	name =  models.CharField(blank=False, max_length=20)
	username = models.CharField(blank=False, max_length=80,unique=True)
	email = models.EmailField(blank=False, max_length=100)
	password = models.CharField(blank=False, max_length=20)
	phone = models.CharField(blank=True, max_length=20)
	address = models.CharField(blank=True, max_length=200)
	image = models.ImageField(blank=True, upload_to='static/Admin/images/user_pic/')
	date_time = models.DateTimeField(auto_now_add=True)



