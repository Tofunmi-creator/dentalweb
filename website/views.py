from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'home.html',{})

def about(request):

    return render(request, 'about.html',{})

def service(request):
    return render(request, 'service.html',{})

def pricing(request):
    return render(request, 'pricing.html',{})

def blog(request):
    return render(request, 'blog.html',{})

def blog_details(request):
    return render(request, 'blog-details.html',{})

def contact(request):
    if request.method=="POST":
        print(request.POST)
        print(str(settings.EMAIL_HOST_USER))
        message_name=request.POST['message-name']
      
        
        message_email=request.POST['message-email']
        message=request.POST['message']
        send_mail(subject=str('Message from: '+str(message_name)+ ', Email: '+str(message_email)),
                  message=message,#message
                  from_email=str(settings.EMAIL_HOST_USER),
                  recipient_list=['johncaul@yahoo.com']
                 
        )

    return render(request, 'contact.html',{})