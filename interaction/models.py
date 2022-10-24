from django.db import models
from django.contrib.auth.models import User
from plants.models import Plant,Garden,Garden_tips


class Action_plant(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    plant=models.ForeignKey(to=Plant,on_delete=models.CASCADE,related_name='actions_plant')
    liked=models.BooleanField(null=True)

    class Meta:
        unique_together=['user','plant'] 


class Action_garden(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    garden=models.ForeignKey(to=Garden,on_delete=models.CASCADE,related_name='actions_garden')
    liked=models.BooleanField(null=True)

    class Meta:
        unique_together=['user','garden'] 


class Action_garden_tips(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    garden_tips=models.ForeignKey(to=Garden_tips,on_delete=models.CASCADE,related_name='actions_garden_tips')
    liked=models.BooleanField(null=True)

    class Meta:
        unique_together=['user','garden_tips'] 



    