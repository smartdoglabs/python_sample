from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.
class BetaInvite(models.Model):
    email = models.EmailField(max_length=254)
    request_date = models.DateTimeField('request_date',default=timezone.now())
    invite_code = models.CharField(max_length=255,null=True,blank=True)
       
    def __str__(self):
        return self.email
          
          
class Workout(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=100)
    workout_date = models.DateTimeField('workout_date')
    distance = models.IntegerField('distance',default=0)
    duration = models.IntegerField('duration',default=0)
    
    def __str__(self):
        return self.name + ":" + self.type + "@" + self.workout_date
    
class Circle(models.Model):
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(User)
    
 
    def __str__(self):
        return self.name + ":" + self.type