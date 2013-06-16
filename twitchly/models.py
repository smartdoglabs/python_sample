from django.db import models
from django.utils import timezone

# Create your models here.
class BetaInvite(models.Model):
    email = models.EmailField(max_length=254)
    request_date = models.DateTimeField('request_date',default=timezone.now())
    invite_code = models.CharField(max_length=255,null=True,blank=True)
       
    def __str__(self):
        return self.email
            