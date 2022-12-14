from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
#import includ

#impport this two packages for media config 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('plants.urls')),
    path('', include('interaction.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
