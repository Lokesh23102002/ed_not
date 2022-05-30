from turtle import fd
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render

from calc.models import fields,calc, Question
from django.contrib.auth.models import User
def fdgdlst(request,field):
    fd=fields.objects.get(name=field)
    gds=[]
    for gd_us in fd.guides.all() :
        gds+=[calc.objects.get(user=gd_us)]
    print(gds)
    return render(request,'guidee/gdlst.html',{'gds':gds,'usrinfo':calc,'fd':fd})

def gdprofile(request,field,guide):
    gd_us=User.objects.get(username=guide)
    gd=calc.objects.get(user=gd_us)
    fd=fields.objects.get(name=field)
    usr=User.objects.get(username=str(request.user))
    if request.method=='GET':
        if request.GET.get('ques') is not None:
            question=request.GET.get('ques')
            print(question)
            return render(request,'guidee/gdconnect.html',{'ques':question,'gd':gd,'connect_asked':False})
        else:
            certs=gd.certificates.all()
            certificates=[]
            for c in certs:
                print(c.fd, fd)
                if c.fd == fd:
                    certificates+=[c]
            print(certs, gd, certificates)
            return render(request,'guidee/gdprofile.html',{'gd':gd,'certificates':certificates,'connect_asked':False})
    elif request.method=='POST':
        print("rp")
        if request.GET.get('ques') is not None:
            question=request.GET.get('ques')
            print(question)
            if 'connect' in request.POST:
                print(question)
                Q=Question(ques=question,guide=gd_us,guidee=usr,fd=fd)
                Q.save()
                gd.questions_byguidees.add(Q)
                us=calc.objects.get(usr=usr)
                us.questions_asked.add(Q)
                connect_asked=True
            elif 'disconnect' in request.POST:
                Q=Question.objects.get(ques=question,fd=fd,guidee=usr,guide=gd_us)
                us=calc.objects.get(usr=usr)
                us.questions_asked.remove(Q)
                Q.delete()
                connect_asked=False
            return render(request,'guidee/gdconnect.html',{'ques':question,'gd':gd,'connect_asked':connect_asked})


            
            