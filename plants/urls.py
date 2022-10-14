from django.urls import path
from .import views
# from .import views
#import include

#add app name
app_name='plants'

urlpatterns = [
    path('', views.index_view,name='index'),
    path('plant/', views.PlantListView.as_view(),name='plants'),
    path('plant/<int:pk>', views.PlantDetailView.as_view(),name='plant'),
    path('garden/', views.GardenListView.as_view(),name='gardens'),
    path('garden/<int:pk>', views.GardenDetailView.as_view(),name='garden'),

    path('garden_tips/', views.Garden_tips_ListView.as_view(),name='garden_tips'),
    path('garden_tips/<int:pk>', views.Garden_tips_DetailView.as_view(),name='garden_tip'),
    
]