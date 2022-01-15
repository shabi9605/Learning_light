from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . models import *
from . forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from payment.models import *

from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

# Create your views here.

def valuable_donation(request):
    if request.method=="POST":
        donation_form=ValuableDonationForm(request.POST)
        if donation_form.is_valid():
            contributor=Contributor.objects.get(user=request.user)
            cp=ValuableDonation(user=request.user,contributor=contributor,type=donation_form.cleaned_data['type'],donation_user=donation_form.cleaned_data['donation_user'])
            cp.save()

            
            return render(request,'valuable_donation_form.html',{'msg':'successfully added donation'})
        else:
            return HttpResponse("Invalid form")
    donation_form=ValuableDonationForm()
    return render(request,'valuable_donation_form.html',{'form':donation_form})


def donation_history(request):
    my_donations=ValuableDonation.objects.filter(user=request.user).order_by('-date')
    
    return render(request,'valuable_donation_history.html',{'my_donations':my_donations})


def arrived_donation(request):
    arrived_donations=ValuableDonation.objects.filter(user=request.user,status='received')
    print(arrived_donations)
    return render(request,'arrived_donations.html',{'arrived_donations':arrived_donations})


def pending_donation(request):
    pending_donations=ValuableDonation.objects.filter(user=request.user,status='pending')
    print(pending_donations)
    return render(request,'pending_donations.html',{'pending_donations':pending_donations})



