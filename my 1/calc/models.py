
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class calc(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=12)
    rans = models.CharField(max_length=12)
    rques = models.CharField(max_length=12)
    birthday=models.DateField()
    token = models.CharField( max_length=200,default='')
    is_varified = models.BooleanField(default=False)
    image = models.FileField(default='profile.png',upload_to='profile_pics')
    

    def __str__(self):
        return self.user.username

    





