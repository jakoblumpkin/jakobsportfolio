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
    # if request.method=='POST':
    #    send_mail('portfolio Subject: '+subject,
    #              'Message: '+message+'\nName: '+name+' \nEmail: '+email,
    #              settings.EMAIL_HOST_USER,
    #              ['lumpkinjakobr@gmail.com'],
    #              fail_silently=False)
    if request.method == 'POST':
        send_mail('portfolio Subject: ' + subject,
        'Message: ' + message + '\nName: ' + name + ' \nEmail: ' + email,
        'Lumpkinjakobr@gmail.com',
        ['Lumpkinjakobr@gmail.com'],
        fail_silently=False)
    return redirect('/')