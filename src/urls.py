from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
#import includ

#impport this two packages for media config 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('plants.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
