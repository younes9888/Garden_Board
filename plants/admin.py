from django.contrib import admin

#import plant model
from .models import Garden_tips, Plant,Garden

# Register your models here.
class PlantAdmin(admin.ModelAdmin):  
      
    #show this arrangment on admin panal
    list_display=('id','title','image','descreption')

class PlantAdmin_garden(admin.ModelAdmin):  
      
    #show this arrangment on admin panal
    list_display=('id','title','image','descreption')


class PlantAdmin_garden_tips(admin.ModelAdmin):  
      
    #show this arrangment on admin panal
    list_display=('id','title','image','descreption','tips_date')

admin.site.register(Plant,PlantAdmin)
admin.site.register(Garden,PlantAdmin_garden)
admin.site.register(Garden_tips,PlantAdmin_garden_tips)
