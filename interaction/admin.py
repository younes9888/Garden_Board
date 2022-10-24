from django.contrib import admin
from .models import Action_garden,Action_garden_tips,Action_plant
# Register your models here.


class ActionModel_plant(admin.ModelAdmin):
    pass

admin.site.register(Action_plant,ActionModel_plant)



class ActionModel_garden(admin.ModelAdmin):
    pass

admin.site.register(Action_garden,ActionModel_garden)



class ActionModel_garden_tips(admin.ModelAdmin):
    pass

admin.site.register(Action_garden_tips,ActionModel_garden_tips)