from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('valuable_donation',views.valuable_donation,name='valuable_donation'),
    path('donation_history',views.donation_history,name='donation_history'),
    path('arrived_donation',views.arrived_donation,name='arrived_donation'),
    path('pending_donation',views.pending_donation,name='pending_donation'),
]