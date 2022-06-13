from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from calc.models import fields, Question, Review, Rating
from chat.models import room



class guideeinfo(models.Model):
    usr=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    fds=models.ManyToManyField(fields,related_name='interested_fields')
    rating=models.FloatField(default=0.0)
    ratings_received=models.ManyToManyField(Rating, related_name="guidee_received", blank=True)
    ratings_given=models.ManyToManyField(Rating, related_name="guidee_rated", blank=True)
    questions_asked=models.ManyToManyField(Question,related_name="questions_asked",blank=True)
    guidee_availablemode=models.IntegerField(default=0)
    guidee_rooms=models.ManyToManyField(room, blank=True,related_name="guidee_rooms")
    rvws_received=models.ManyToManyField(Review,blank=True,related_name="reviews_received_bygde")
    rvws_posted=models.ManyToManyField(Review,blank=True, related_name="reviews_posted_bygde")

    def __str__(self):
        return str(self.usr)