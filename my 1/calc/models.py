
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class fields(models.Model):
    name=models.CharField(max_length=200,primary_key=True)
    guides=models.ManyToManyField(User,related_name='guides',blank=True)
    guidees=models.ManyToManyField(User,related_name='guidees',blank=True)
    def __str__(self):
        return str(self.name)

    def guides_list(self):
        return ",".join([str(i) for i in self.guides.all()])
    def guidees_list(self):
        return ",".join([str(i) for i in self.guidees.all()])

class certificates(models.Model):
    fd=models.ForeignKey(fields,on_delete=models.CASCADE)
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    issuedby=models.CharField(max_length=500,blank=True)
    certificate=models.FileField(upload_to='certificates',blank=True)
    def __str__(self):
        return str(self.usr)+"_"+str(self.fd)

class calc(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=12)
    birthday=models.DateField()
    token = models.CharField( max_length=200,default='')
    guide_rating=models.FloatField(default=0.0)
    guidee_rating=models.FloatField(default=0.0)
    level=models.IntegerField(default=0)
    level=models.IntegerField(default=0)
    is_varified = models.BooleanField(default=False)
    certificates=models.ManyToManyField(certificates,blank=True)
    image = models.FileField(default ="profile.png" ,upload_to='profile_pics')
    fdsneeded=models.ManyToManyField(fields,related_name='interested_fields')
    fdsexpert=models.ManyToManyField(fields,related_name='expertise_fields')
    
    def fdsneeded_list(self):
        return ",".join([str(i) for i in self.fdsneeded.all()])
    def fdsexpert_list(self):
        return ",".join([str(i) for i in self.fdsexpert.all()])

    def __str__(self):
        return self.user.username

    
class Question(models.Model):
    ques=models.TextField()
    fd=models.ForeignKey(fields,on_delete=models.CASCADE)
    guidee=models.ForeignKey(User,related_name="guidee", on_delete=models.CASCADE)
    guide=models.ForeignKey(User, related_name="guide",on_delete=models.CASCADE)
    time_asked=models.DateTimeField()
    status=models.IntegerField(default=0)
    class Meta:
        ordering=['-time_asked']




