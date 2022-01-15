from django import forms
from django.db.models import fields
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=('username','password1','password2')
        labels=('password1','password','password2','confirm password')


class InstitutionForm(forms.ModelForm):
    class Meta:
        model=Institution
        fields=('name','phone','state','district','pincode','enroll_no','type')



class StudentForm(forms.ModelForm):
    education=forms.CharField(label='class/course')
    class Meta:
        model=Student
        fields=('dob','education','roll_no','local_body','state','district','pincode','address','phone','father_name','mother_name','institution')


class ContributorForm(forms.ModelForm):
    class Meta:
        model=Contributor
        fields=('state','district','pincode','phone','donation_user')


class RequestForm(forms.ModelForm):
    class Meta:
        model=Request
        fields=('request','number','phone')


class ApprovestudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('status',)



class ApproveInstitution(forms.ModelForm):
    class Meta:
        model=Institution
        fields=('status',)