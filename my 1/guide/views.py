from django.utils import timezone
from unicodedata import name
from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime

from calc.models import usrinfo, fields, Question, Review, Rating
from chat.models import room


def gde_cntct_lst(request,field):
    fd=fields.objects.get(name=field)
    usr=User.objects.get(username=str(request.user))
    questions=[]
    show=request.GET.get('show')
    if show=='chat_gde':
        tp='chat'
        gde_lst=[]
        for rm in usr.guideinfo.guide_rooms.all():
            gde_lst+=[rm]
        return render(request,'gde_contact_lst.html',{'fd':fd,'gde_lst':gde_lst,'type':tp})
    elif show=='not seen':
        tp='ques'
        shl=[0,]
    elif show=='all':
        tp='ques'
        shl=[1,0]
    if show=='new':
        tp='ques'
        new=True
        for q in usr.guideinfo.questions_byguidees.all():
            print(q.time_asked > usr.guideinfo.lastgdelstseen)
            if q.fd == fd and q.time_asked > usr.guideinfo.lastgdelstseen :
                questions+=[q]
                print(q.guidee.guideeinfo.rating)
        print(questions)
    
    else:
        new=False
        for q in usr.guideinfo.questions_byguidees.all():
            if q.fd == fd and q.status in shl:
                questions+=[q]
               
    usr.guideinfo.lastgdelstseen=timezone.now()
    usr.guideinfo.save()
    return render(request,'gde_contact_lst.html',{'fd':fd,'questions':questions,'new':new,'type':tp})

def gdeprofile(request,field,guidee):
    fd=fields.objects.get(name=field)
    usr=User.objects.get(username=str(request.user))
    gde=User.objects.get(username=guidee)

    ques=request.GET.get('ques')
    Q=Question.objects.get(fd=fd,guide=usr,guidee=gde,ques=ques)
    if request.method=='POST':
        if 'rvw' in request.POST:
            rvw=request.POST['rvw']
            rvw_object=Review.objects.create(rvw=rvw,gd=usr,gde=gde,status="gd_gde")
            usr.guideinfo.rvws_posted.add(rvw_object)
            usr.guideinfo.save()
            gde.guideeinfo.rvws_received.add(rvw_object)
            gde.guideeinfo.save()
        elif 'rate' in request.POST:
            r=request.POST['rating']
            print(r)
            for rating in gde.guideeinfo.ratings_received.all():
                print('rating')
                print(rating.gd == usr)
                print('rating end')
                if rating.gd == usr:
                    t='ch'
                    break
            else:
                t='add'
            print(t)
            gde_r_c=gde.guideeinfo.ratings_received.all().count()
            if t=='ch':
                r_object=Rating.objects.get(gd=usr, gde=gde,status='gd_gde')
                print(r_object.value,float(r))
                ch_r=((-(r_object.value))+float(r))/(gde_r_c)
                print(ch_r)
                f_r=(gde.guideeinfo.rating)+ch_r
                r_object.value=float(r)
                r_object.save()
            elif t=='add':
                r_s=(gde.guideeinfo.rating)*(gde_r_c)
                r_s+=float(r)
                f_r=float(r_s/(gde_r_c+1))
                r_object=Rating.objects.create(value=float(r),gd=usr,gde=gde,status='gd_gde')
                usr.guideinfo.ratings_given.add(r_object)
                usr.guideinfo.save()
                gde.guideeinfo.ratings_received.add(r_object)
            gde.guideeinfo.rating=f_r
            gde.guideeinfo.save()
            

    else:
        Q.status=1
        Q.save()
        print(Q)
    rvws=gde.guideeinfo.rvws_received.all()[::-1]
    return render(request,'gdeprofile.html',{'ques':Q,'gde':gde,'rvws':rvws, 'fd':fd})
    
    