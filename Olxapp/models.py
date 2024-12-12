from django.db import models
# for authantication
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	# #@daverobb2011
	# class Meta:
	# 	verbose_name_plural = 'categories'
class Olx(models.Model):
    # authentication
    user = models.ForeignKey(User,on_delete = models.SET_NULL,null = True,blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length = 50)
    Description = models.TextField()
    SET_A_PRICE = models.CharField(max_length =50)
    Upload_image = models.ImageField(upload_to="image/",max_length=250,null=True,default=None)
    list_date = models.DateField(auto_now_add=True)
    Approved = models.BooleanField('Approved',default=False)
    def __str__(self):
        return self.title
class Image(models.Model):
    listing = models.ForeignKey(Olx, related_name='images', on_delete=models.CASCADE)
    Upload_image = models.ImageField(upload_to='image/')
# Create your models here.




# Create your models here.
