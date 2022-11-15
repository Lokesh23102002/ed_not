from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

from calc.models import Question, fields



class room(models.Model):
    guide=models.ForeignKey(User, on_delete=models.CASCADE, related_name="usr1", null=True)
    guidee=models.ForeignKey(User, on_delete=models.CASCADE, related_name="usr2", null=True)
    ques=models.ForeignKey(Question, on_delete=models.CASCADE, blank= True, null= True)
    fd=models.ForeignKey(fields, on_delete=models.CASCADE, blank=True, null=True)
    room_name=models.CharField(max_length=500)
    status=models.TextField(max_length=20, default="r")
    def __str__(self):
        return str(self.room_name)

class message(models.Model):
    mssg=models.CharField(max_length=5000)
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender", blank=True, null=True)
    receiver=models.ForeignKey(User, on_delete=models.CASCADE,related_name="receiver", blank=True, null=True)
    status=models.CharField(max_length=4)
    rm=models.ForeignKey(room, on_delete=models.CASCADE, blank=True, null=True)
    time_send=models.DateTimeField(auto_now_add=True)
    time_received=models.DateTimeField(auto_now=True)