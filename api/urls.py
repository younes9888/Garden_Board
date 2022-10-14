from django.urls import path
#import includ
from . import views

app_name='api'

urlpatterns = [
    path('plants/', views.PlantsListApiView.as_view(),name='PlantsListApiView'),
    path('plants/<int:id>/', views.PlantsDetailApiView.as_view(),name='PlantsDetailApiView'),
] 