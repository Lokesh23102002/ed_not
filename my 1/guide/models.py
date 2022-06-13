from django.db import models
from django.contrib.auth.models import User

from calc.models import fields, Question, Review, Rating
from chat.models import room
from django.utils import timezone

# Create your models here.
def user_directory_path(instance, filename):
    ext=filename.split('.')[-1]
    return '{0}/{1}/{2}'.format(instance.usr.id,'Certificates',filename)

class Certificate(models.Model):
    fd=models.ForeignKey(fields,on_delete=models.CASCADE)
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    issuedby=models.CharField(max_length=500,blank=True)
    certificate=models.FileField(upload_to='certificates',blank=True)
    def __str__(self):
        return str(self.usr)+"_"+str(self.fd)



class guideinfo(models.Model):
    usr=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    fds=models.ManyToManyField(fields,related_name='expertise_fields',blank=True)
    rating=models.FloatField(default=0.0)
    ratings_received=models.ManyToManyField(Rating, related_name="guide_received", blank=True)
    ratings_given=models.ManyToManyField(Rating, related_name="guide_rated", blank=True)
    level=models.IntegerField(default=0)
    certificates=models.ManyToManyField(Certificate,blank=True)
    questions_byguidees=models.ManyToManyField(Question,related_name='questions_byguidees',blank=True)
    connectmode=models.IntegerField(default=0)
    lastgdelstseen=models.DateTimeField(default=timezone.now())
    guide_rooms=models.ManyToManyField(room, blank=True,related_name="guide_rooms")
    rvws_received=models.ManyToManyField(Review,blank=True,related_name="reviews_received_bygd")
    rvws_posted=models.ManyToManyField(Review,blank=True, related_name="reviews_posted_bygd")

    def __str__(self):
        return str(self.usr)