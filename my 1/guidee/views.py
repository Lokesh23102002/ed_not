from multiprocessing.sharedctypes import Value
from telnetlib import STATUS
from turtle import fd
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank

from calc.models import fields,usrinfo, Question, Review, Rating

from django.contrib.auth.models import User

from .forms import Rvw_form

def gdlst(request,field=None):
    if field==None:
        usr=User.objects.get(username=str(request.user))
        rms=[]
        for rm in usr.guideeinfo.guidee_rooms.all():
            if rm.status == "r":
                rms+=[rm]
        lst_type="contact_lst"
        return render(request,'guidee/ongoing_queslst.html',{'rms':rms,'usrinfo':usrinfo,'type':lst_type})
    else:        
        fd=fields.objects.get(name=field)
        print(fd)
        gds=fd.guides.all()
        print(gds)
        lst_type="fd_gd_lst"
        return render(request,'guidee/gdlst.html',{'gds':gds,'usrinfo':usrinfo,'fd':fd,'type':lst_type})

def r_queslst(request,field=None):
    fd=fields.objects.get(name=field)
    question=request.GET.get('ques')
    print(question)
    related_ques= Question.objects.filter(ques=question,fd=fd)
    print(related_ques)
    return render(request,'guidee/queslst.html',{'ques':question,'fd':fd, 'related_ques':related_ques})



def gdprofile(request,field,guide):
    gd=User.objects.get(username=guide)
    fd=fields.objects.get(name=field)
    usr=User.objects.get(username=str(request.user))
    if request.method=='GET':
        if request.GET.get('ques') is not None:
            question=request.GET.get('ques')
            checkques=Question.objects.filter(ques=question,guide=gd,guidee=usr,fd=fd).exists()
            
            print(checkques)
            if(checkques == True):
                Qu=Question.objects.get(ques=question,guide=gd,guidee=usr,fd=fd)
            else:
                Qu=Question(ques=question,guide=gd,guidee=usr,fd=fd)
                Qu.save()
            related_ques= Question.objects.filter(guide=gd,ques=question,fd=fd)
            exclude=related_ques.exclude(guidee=usr)
            return render(request,'guidee/gdconnect.html',{'ques':Qu,'gd':gd,'fd':fd, 'connect_asked':False, 'related_ques':exclude})
        else:
            certs=gd.guideinfo.certificates.all()
            certificates=[]
            for c in certs:
                print(c.fd, fd)
                if c.fd == fd:
                    certificates+=[c]
            print(certs, gd, certificates)
            rvw_form=Rvw_form()
            return render(request,'guidee/gdprofile.html',{'gd':gd,'certificates':certificates,'connect_asked':False, 'rvw_form':rvw_form})
    elif request.method=='POST':
        print(request)
        if request.GET.get('ques') is not None:
            question=request.GET.get('ques')
            print(question)
            if 'sending_ques' in request.POST:
                print(question)
                Q=Question.objects.get(ques=question,guide=gd,guidee=usr,fd=fd)
                Q.save()
                gd.guideinfo.questions_byguidees.add(Q)
                usr.guideeinfo.questions_asked.add(Q)
                ques_sent=True
            elif 'unsending_ques' in request.POST:
                Q=Question.objects.get(ques=question,fd=fd,guidee=usr,guide=gd)
                usr.guideeinfo.questions_asked.remove(Q)
                gd.guideinfo.questions_byguidees.remove(Q)
                ques_sent=False
            
            related_ques= Question.objects.filter(guide=gd,ques=question,fd=fd)
            exclude=related_ques.exclude(guidee=usr)
            return render(request,'guidee/gdconnect.html',{'ques':Q,'gd':gd, 'fd':fd, 'ques_sent':ques_sent,'related_ques':exclude})
        elif 'rvw_post' in request.POST:
            rvw=request.POST['rvw']
            rvw_object=Review.objects.create(rvw=rvw,gd=gd,gde=usr,status="gde_gd")
            usr.guideeinfo.rvws_posted.add(rvw_object)
            usr.guideeinfo.save()
            gd.guideinfo.rvws_received.add(rvw_object)
            gd.guideinfo.save()
            rvw_form=Rvw_form()
            certs=gd.guideinfo.certificates.all()
            certificates=[]
            for c in certs:
                print(c.fd, fd)
                if c.fd == fd:
                    certificates+=[c]
            return render(request,'guidee/gdprofile.html',{'gd':gd,'certificates':certificates,'connect_asked':False, 'rvw_form':rvw_form})
        elif 'rate' in request.POST:
            r=request.POST['rating']
            print(r)
            for rating in gd.guideinfo.ratings_received.all():
                print('rating')
                print(rating.gde == usr)
                print('rating end')
                if rating.gde == usr:
                    t='ch'
                    break
            else:
                t='add'
            gd_r_c=gd.guideinfo.ratings_received.all().count()
            if t=='ch':
                r_object=Rating.objects.get(gd=gd, gde=usr,status='gde_gd')
                print(r_object.value,float(r))
                ch_r=((-(r_object.value))+float(r))/(gd_r_c)
                print(ch_r)
                f_r=(gd.guideinfo.rating)+ch_r
                r_object.value=float(r)
                r_object.save()
            elif t=='add':
                r_s=(gd.guideinfo.rating)*(gd_r_c)
                r_s+=float(r)
                f_r=float(r_s/(gd_r_c+1))
                r_object=Rating.objects.create(value=float(r),gd=gd,gde=usr,status='gde_gd')
                usr.guideeinfo.ratings_given.add(r_object)
                usr.guideeinfo.save()
                gd.guideinfo.ratings_received.add(r_object)                
            gd.guideinfo.rating=f_r
            gd.guideinfo.save()
            rvw_form=Rvw_form()
            certs=gd.guideinfo.certificates.all()
            certificates=[]
            for c in certs:
                print(c.fd, fd)
                if c.fd == fd:
                    certificates+=[c]
            return render(request,'guidee/gdprofile.html',{'gd':gd,'certificates':certificates,'connect_asked':False, 'rvw_form':rvw_form})


            
            

            
            


            
            