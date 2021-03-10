
from django.db import models
from django.contrib.auth.models import User

class Competition(models.Model):
    title = models.CharField(max_length=100,default="")
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to='images/thumbnail/',blank=True)
    def __str__(self):
        return self.title


class SubmitCompetition(models.Model):

    title = models.CharField(max_length=100,default="")
    medium = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/image/')

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title