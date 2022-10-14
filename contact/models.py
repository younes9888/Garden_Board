from django.db import models



class Info(models.Model):
    place=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    email=models.EmailField()

    class Meta:
        pass

    def __str__(self):
        return self.email