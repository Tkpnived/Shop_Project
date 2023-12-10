from django.db import models

# Create your models here.
class logindb(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
class contactdb(models.Model):
    yourname=models.CharField(max_length=100)
    youremail=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
class cart(models.Model):
    Images=models.ImageField(null=True)


    product=models.CharField(max_length=100,null=True)
    singleprice = models.CharField(max_length=100, null=True)
    price =models.CharField(max_length=100,null=True)
    Qty=models.CharField(max_length=100,null=True)
