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
    leader = models.ForeignKey(User,related_name="leader_user")
    repeat_type = models.CharField(max_length=25)
    initial_date = models.DateTimeField('initial_date')
    price = models.FloatField()
    
    def __str__(self):
        return self.name + ":" + self.type
    
class CircleMeeting(models.Model):
    circle = models.ForeignKey(Circle)
    meeting_date = models.DateTimeField('meeting_date')
    attending_users = models.ManyToManyField(User)
    price_override = models.FloatField()
    
    def __str__(self):
        return "Meeting for"+ self.circle.name + "on" + self.meeting_date
    