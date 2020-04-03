from django.db import models
from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError

CATOGORY = (
("Pro Apps","Pro Apps"),
 ("Mod Apps","Mod Apps"),
 ("Tv Serias","Tv Serias"),
 ("Films","Films"),
 ("Softwears", "Softwears"),
)
# Create your models here.
class posts(models.Model):
    id = models.AutoField(primary_key=True)
    username_id =models.ForeignKey("auth.USER",on_delete=models.CASCADE,)
    title=models.CharField(max_length =20,blank=False)
    quickdes = models.CharField(max_length=60)
    description =models.TextField()
    image = models.CharField(max_length=300,blank=False)
    catagorye = models.CharField(max_length=50,choices=CATOGORY)
    version= models.FloatField(default=0.01)
    date_and_time = models.DateTimeField(auto_now=True)

 


class requests(models.Model):
    id = models.AutoField(primary_key=True)
    username_id =models.ForeignKey("auth.USER",on_delete=models.CASCADE,)
    catogory =models.CharField(max_length=50,choices=CATOGORY)
    product_name = models.CharField(max_length=50)
    version= models.FloatField(default=0.01)
    dev_company = models.CharField(max_length =70)

class font(models.Model):
    id=  models.AutoField(primary_key=True)
    username_id =models.ForeignKey("auth.USER",on_delete=models.CASCADE)
    title =title=models.CharField(max_length =30,blank=False)
    url = models.CharField(max_length=300)
    image = models.URLField(blank=False)
    
    
    
