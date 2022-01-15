from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.http import request
from phonenumber_field.modelfields import PhoneNumberField

from donation.models import *
from django.utils import timezone

# Create your models here.


class Institution(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phone=PhoneNumberField()
    state=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    pincode=models.IntegerField()
    enroll_no=models.CharField(max_length=50,null=True,blank=True)
    private='private'
    government='government'
    aided='aided'
    types=[
        (private,'private'),
        (government,'government'),
        (aided,'aided')
    ]
    type=models.CharField(max_length=50,choices=types,null=True,blank=True,default=private)
    status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)


class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dob=models.CharField(max_length=50)
    education=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    pincode=models.IntegerField()
    address=models.CharField(max_length=50)
    phone=PhoneNumberField()
    local_body=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    institution=models.ForeignKey(Institution,on_delete=models.CASCADE,null=True,blank=True)
    roll_no=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)


class Contributor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    state=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    pincode=models.IntegerField()
    phone=PhoneNumberField()
    group='group'
    organization='organization'
    person='person'

    donation_users=[
        (group,'group'),
        (organization,'organization'),
        (person,'person')
    ]
    donation_user=models.CharField(max_length=50,choices=donation_users,default=person)
    def __str__(self):
        return str(self.user.username)





class Request(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    laptop='laptop'
    book='book'
    notes='notes'
    pen='pen'
    cash='cash'
    uniform='uniform'
    speaker='speaker'
    valuables=[
        (laptop,'laptop'),
        (book,'book'),
        (notes,'notes'),
        (pen,'pen'),
        (cash,'cash'),
        (uniform,'uniform'),
        (speaker,'speaker')

    ]
    request=models.CharField(max_length=50,choices=valuables,default=cash,null=True,blank=True)
    number=models.CharField(max_length=50,null=True,blank=True)
    phone=PhoneNumberField()
    
    processing='processing'
    accepted='accepted'
    rejected='rejected'
    statuses=[
        
        (processing,'processing'),
        (accepted,'accepted'),
        (rejected,'rejected')

    ]
    status=models.CharField(max_length=30,choices=statuses,default=processing)
    assign=models.BooleanField(default=False,null=True,blank=True)
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)




