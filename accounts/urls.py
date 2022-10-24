from django.urls import path
#import includ
from .views import RegisterView,PasswordResetDoneView

from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('register/', RegisterView.as_view(),name='register'),
  path('reset_password/', auth_views.PasswordResetView.as_view(), name ='reset_password'),
  path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
  path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
  path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
]
