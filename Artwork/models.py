from django.db import models
from Profile.models import User

from django.contrib.auth.models import User


# Create your models here.
class Artwork(models.Model):
    title = models.CharField(max_length=100, default="")

    medium = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    art_description = models.TextField(max_length=3000, null=True)
    art = models.ImageField(upload_to='images/art/')

    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.title



