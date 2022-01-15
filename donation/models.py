from django.db import models
from django.contrib.auth.models import User
from django.http import request
from phonenumber_field.modelfields import PhoneNumberField

from django.utils import timezone

#from account.models import Contributor

# Create your models here.
class Valuable(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

class ValuableDonation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    type=models.ForeignKey(Valuable,on_delete=models.CASCADE,null=True,blank=True)
    #contributor=models.ForeignKey(Contributor,on_delete=models.CASCADE,null=True,blank=True)
    contributor=models.ForeignKey("account.Contributor",on_delete=models.CASCADE,null=True,blank=True)
    group='group'
    organization='organization'
    person='person'

    donation_users=[
        (group,'group'),
        (organization,'organization'),
        (person,'person')
    ]
    donation_user=models.CharField(max_length=50,choices=donation_users,default=person)
    pending='pending'
    processing='processing'
    received='received'
    statuses=[
        (pending,'pending'),
        (processing,'processing'),
        (received,'received')

    ]
    status=models.CharField(max_length=30,choices=statuses,default=pending)
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)

    
