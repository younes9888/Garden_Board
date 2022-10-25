from datetime import datetime
from email.mime import audio
from time import time
from django.db import models
from django.contrib.auth.models import User


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

class Comment(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    plant_comment=models.ForeignKey(to=Plant,on_delete=models.CASCADE)
    date_comment=models.DateField(auto_now_add=True)
    content=models.TextField()
        
    def __str__(self):
        return str(self.user)

class Comment_garden(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    plant_comment=models.ForeignKey(to=Garden,on_delete=models.CASCADE)
    date_comment=models.DateField(auto_now_add=True)
    content=models.TextField()
        
    def __str__(self):
        return str(self.user)

class Comment_garden_tips(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    plant_comment=models.ForeignKey(to=Garden_tips,on_delete=models.CASCADE)
    date_comment=models.DateField(auto_now_add=True)
    content=models.TextField()
        
    def __str__(self):
        return str(self.user)


        