from datetime import datetime
from time import time
from django.db import models
import datetime as dt

# Create your models here.

class Plant(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField()
    descreption=models.TextField()

    def __str__(self):
        return self.title


class Garden(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField()
    descreption=models.TextField()

    def __str__(self):
        return self.title
    
class Garden_tips(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField()
    descreption=models.TextField()
    tips_date=models.DateField(dt.datetime.now())

    def __str__(self):
        return self.title
        