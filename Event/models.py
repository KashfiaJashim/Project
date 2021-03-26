from django.db import models
from django.contrib.auth.models import User



class Review(models.Model):
    RATING_OPTIONS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    rating = models.CharField(max_length=10, choices = RATING_OPTIONS, default='4')
    comment = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.rating



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

    reviews = models.ManyToManyField(Review)

    def __str__(self):
        return self.title