from fnmatch import fnmatchcase
from lib2to3.pgen2 import token
import uuid
from django import http
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse_lazy
from sympy import Q
from django.views.decorators.cache import never_cache
from my.settings import BASE_DIR
from .models import usrinfo,fields
from django.conf import settings
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from guide.models import guideinfo
from guidee.models import guideeinfo
from guide.models import Certificate
# Create your views here
@never_cache
def home(request):
    my_user = request.user

    is_user_logged = my_user.is_authenticated

    if is_user_logged == True:
        return redirect('guide')
  
    
    if request.method ==  "POST" :
        username= request.POST.get("user")
        password = request.POST.get("passw")
        user_obj = User.objects.filter(username=username).first()
        profile_obj = usrinfo.objects.filter(usr=user_obj).first()

        user=auth.authenticate(username=username,password=password)

        

        if user is not None :
            if profile_obj.is_varified == False:
                messages.success(request, 'Your email has not been verified please verify your email')
                return redirect('guide')
            else:
                auth.login(request,user)
                return redirect('guide')
                
        else:
            messages.success(request, 'Invalid credentials try again')
            return redirect('home')
            
    else:

        return render(request,'Signin.html')

def dash(request):
    if request.user.is_authenticated == False:
        return redirect('home')
    print(request.POST)
    if request.method == 'POST' and ('remc' in request.POST):
        field=request.POST.get('remc')
        cert=Certificate.objects.get(certificate = field)
        cert.delete()
        print(field)
    
    
        
    if request.method == 'POST' and ('fields' in request.POST) and request.FILES.get('uploadd'):
        field=fields.objects.get(name=request.POST.get('fields'))
        uploadd = request.FILES.get('uploadd')
        use=request.user
        cert=Certificate(fd=field,usr=use,certificate = uploadd)
        cert.save()
     
    print(request.POST)
    if request.method == 'POST' and request.FILES.get('upload') :
        upload = request.FILES.get('upload')
        instance=request.user
        if(instance.usrinfo.image.path != (str(BASE_DIR) + "\media\profile.png")):
            instance.usrinfo.image.delete()
        instance.usrinfo.image = upload
        instance.usrinfo.save()

        return redirect('dash')
    cert = request.user.certificate_set.all()
    
    context={'certificate':cert}
    return render(request , "home.html", context)

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

        #if User.objects.filter(email=email).first():
            #messages.error(request, 'Email already in use')
            #return redirect('signup')

        user = User.objects.create_user(username=username,email=email,password=password)
        user.first_name = name
        user.last_name = surname
        user.save()
        tokens=str(uuid.uuid4())
        extra = usrinfo(usr=user,mobile=phoneno,birthday=dob,token=tokens)
        extra.save()
        guideinf=guideinfo(usr=user)
        guideeinf=guideeinfo(usr=user)
        guideinf.save()
        guideeinf.save()

        sendmail(email,tokens)
        return HttpResponse('verification link has been sent on your email please verify to login')


    return render(request, "signup.html")

def signout(request):
    auth.logout(request)
    return redirect('home')

def guide(request):
    if request.user.is_authenticated == False:
        return redirect('home')
    print(request.POST)
    if request.method=="POST":
        if 'submitx' in request.POST:
            for i in request.POST.getlist('fdsexpert'):
                field=fields.objects.get(name=i)
                request.user.guideinfo.fds.add(field)
                field.guides.add(request.user)
                field.save()
                request.user.usrinfo.save()
        elif 'submitn' in request.POST:
             for i in request.POST.getlist('fdsneeded'):
                field=fields.objects.get(name=i)
                request.user.guideeinfo.fds.add(field)
                field.guidees.add(request.user)
                field.save()
                request.user.usrinfo.save()
        elif 'remx' in request.POST:
            i=request.POST.get('remx')
            field=fields.objects.get(name=i)
            request.user.guideinfo.fds.remove(field)
            field.guides.remove(request.user)
            field.save()
            request.user.usrinfo.save()
        elif 'remn' in request.POST:
            i=request.POST.get('remn')
            field=fields.objects.get(name=i)
            request.user.guideeinfo.fds.remove(field)
            field.guidees.remove(request.user)
            field.save()
            request.user.usrinfo.save()
        elif 'ch_connectmode' in request.POST: 
            print('Yes')
            if request.user.guideinfo.connectmode==0:
                request.user.guideinfo.connectmode=1
                request.user.guideinfo.save()

            elif request.user.guideinfo.connectmode==1:
                request.user.guideinfo.connectmode=0
                request.user.guideinfo.save()
    notseengderms = []
    for rm in request.user.guideeinfo.guidee_rooms.all():
        for mssg in rm.message_set.all():
            print(mssg.status)
            if mssg.status=="gd1":
                print(rm)
                print(mssg.mssg, mssg.status)
                notseengderms +=[rm]
                break

    guides = fields.objects.all()
    return render(request,"Guide.html",{'fields':guides,'notseengderms':notseengderms})
    
def sendmail(email,token):
    subject = "your account needs to be verified"
    message = f'Hi paste the link to verify your account http://192.168.137.1:8000/verify/{token}' 
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)


def verify(request, token):
    profile_obj = usrinfo.objects.filter(token=token).first()
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

