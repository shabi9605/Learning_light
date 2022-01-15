from django import forms
from django.db.models import fields
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ValuableDonationForm(forms.ModelForm):
    group='group'
    organization='organization'
    person='person'

    donation_users=[
        (group,'group'),
        (organization,'organization'),
        (person,'person')
    ]
    donation_user=forms.ChoiceField(required=True,choices=donation_users)
    class Meta:
        model=ValuableDonation
        fields=('type','donation_user',)