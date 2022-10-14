from django.urls import path
from .import views
# from .import views
#import include

#add app name
app_name='contact'

urlpatterns = [
    path('', views.contact_views,name='contact_views'),
  
]