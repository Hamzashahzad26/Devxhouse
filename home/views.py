from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import *


from django.core.mail import send_mail
from devxhouse.settings import EMAIL_HOST_USER 
# Create your views here.


def home(request):
    return render(request, "index.html")


def portfolio(request):
    return render(request, "portfolio.html")
    

def contact(request):
    if request.method == "POST":
        name = str(
            request.POST.get("name"),
        )
        email = str(
            request.POST.get("email"),
        )
        subject = str(
            request.POST.get("subject"),
        )
        message = str(
            request.POST.get("message"),
        )
        contact = Contact(
            name=name, email=email, subject=subject, message=message, date=datetime.today()
        )
        contact.save()
        send_mail(
            "User Data: ",
            "mew message is sent",
            "hamzashahzad2600@gmail.com",
            ["hamzashahzad26@gmail.com"],
            fail_silently= False
            )
        print(EMAIL_HOST_USER)
        
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")

