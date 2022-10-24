from datetime import datetime
from time import time
from django.db import models


# Create your models here.

class Plant(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField()
    descreption=models.TextField()
    uploaded_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Garden(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField()
    descreption=models.TextField()
    uploaded_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
class Garden_tips(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField()
    descreption=models.TextField()
    tips_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.title
        