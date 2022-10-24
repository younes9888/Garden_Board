from django.urls import path
from .import views
# from .import views
#import include

#add app name
app_name='interaction'

urlpatterns = [
   
    path('plant/<int:plant_id>/action', views.LikeplantView.as_view(),name='like_plant'),
    path('garden/<int:garden_id>/action', views.LikegardenView.as_view(),name='like_garden'),
    path('garden_tips/<int:garden_tips_id>/action', views.LikeGarden_tips_View.as_view(),name='like_garden_tip'),
    
]