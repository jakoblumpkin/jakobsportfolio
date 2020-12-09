from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request, 'index.html')

def sendemail(request):
    print(request.POST)
    message=request.POST['message']
    subject=request.POST['subject']
    email=request.POST['email']
    name=request.POST['name']
    if request.method=='POST':
       send_mail('portfolio Subject: '+subject,
                 'Message: '+message+' Name: '+name+' Email: '+email,
                 settings.EMAIL_HOST_USER,
                 ['lumpkinjakobr@gmail.com'],
                 fail_silently=False)
       # send_mail('Jakob\'s Portfolio',
       #           f'Hey {name} I have gotten your message published on \'Jakob\'s portfolio\' '
       #           f' website. I will be reaching out to you shortly.',
       #           settings.EMAIL_HOST_USER,
       #           [email],
       #           fail_silently=False)
    return redirect('/')