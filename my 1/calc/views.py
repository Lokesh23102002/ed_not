from fnmatch import fnmatchcase
from lib2to3.pgen2 import token
import uuid
from django import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from sympy import Q

from my.settings import BASE_DIR
from .models import calc
from django.conf import settings
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
# Create your views here.
def home(request):
    my_user = request.user

    is_user_logged = my_user.is_authenticated

    if is_user_logged == True:
        return redirect('dash')
    
    if request.method ==  "POST" :
        username= request.POST.get("user")
        password = request.POST.get("passw")
        user_obj = User.objects.filter(username=username).first()
        profile_obj = calc.objects.filter(user=user_obj).first()

        user=auth.authenticate(username=username,password=password)

        

        if user is not None :
            if profile_obj.is_varified == False:
                messages.success(request, 'Your email has not been verified please verify your email')
                return redirect('home')
            else:
                auth.login(request,user)
                return redirect('dash')   
                
        else:
            messages.success(request, 'Invalid credentials try again')
            return redirect('home')
            
    else:

        return render(request,'Signin.html')

def dash(request):
    if request.user.is_authenticated == False:
        return redirect('home')

    if request.method == 'POST' and request.FILES.get('upload'):
        upload = request.FILES.get('upload')
        instance=request.user
        print(str(BASE_DIR))
        if(instance.calc.image.path != (str(BASE_DIR) + "\media\profile.png")):
            instance.calc.image.delete()
        instance.calc.image = upload
        instance.calc.save()

        return redirect('dash')
    
    return render(request , "home.html")

def signup(request):

    if request.method ==  "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        phoneno = request.POST.get("phoneno")
        dob = request.POST.get("dob")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email=request.POST.get("email")
        
        
        if User.objects.filter(username=username).first() and User.objects.filter(email=email).first():
            messages.error(request, 'Username and email already exist')
            return redirect('signup')

        if User.objects.filter(username=username).first():
            messages.error(request, 'Username already exist')
            return redirect('signup')

        if User.objects.filter(email=email).first():
            messages.error(request, 'Email already in use')
            return redirect('signup')

        user = User.objects.create_user(username=username,email=email,password=password)
        user.first_name = name
        user.last_name = surname
        user.save()
        tokens=str(uuid.uuid4())
        extra = calc(user=user,mobile=phoneno,birthday=dob,token=tokens)
        extra.save()

        sendmail(email,tokens)
        return HttpResponse('verification link has been sent on your email please verify to login')


    return render(request, "signup.html")

def signout(request):
    auth.logout(request)
    return redirect('home')

def guide(request):
    return render(request,"Guide.html")

def sendmail(email,token):
    subject = "your account needs to be verified"
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}' 
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)


def verify(request, token):
    profile_obj = calc.objects.filter(token=token).first()
    if profile_obj:
        if profile_obj.is_varified == True:
            messages.success(request, 'Your email has already been verified')
            return redirect('home')
        else:
            profile_obj.is_varified = True
            profile_obj.save()
            messages.success(request, 'Your email has been verified now you can login')
            return redirect('home')
    else:
        return HttpResponse('error')
    
