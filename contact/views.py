#from .models import Contact
import configparser
from pyexpat import model
from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def contact_views(request):
    myinfo=Info.objects.first()
    if request.method=='POST':
        subject=request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(subject,message,email,[settings.EMAIL_HOST_USER])

    return render(request,'contact.html',context={'myinfo':myinfo})






