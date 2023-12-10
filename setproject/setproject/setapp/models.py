from django.db import models

# Create your models here.

class setdb(models.Model):

    CategoryName = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Image = models.ImageField()


class prodb(models.Model):
    CategoryName = models.CharField(max_length=100)
    Name=models.CharField(max_length=100)
    Price=models.IntegerField()
    Description = models.CharField(max_length=100)

    Image = models.ImageField()
