from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),
    path('student_register',views.student_register,name='student_register'),
    path('institution_register',views.institution_register,name='institution_register'),
    path('contributor_register',views.contributor_register,name='contributor_register'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('profile',views.profile,name='profile'),
    path('contributordashboard',views.contributordashboard,name='contributordashboard'),
    path('request_add',views.request_add,name='request_add'),
    path('accepted_request',views.request,name='accepted_request'),
    path('donation_history',views.donation_history,name='donation_history'),
    path('view_request',views.view_request,name='view_request'),

    path('view_our_students',views.view_our_students,name='view_our_students'),
    path('approve_student/<int:id>',views.approve_student,name='approve_student'),

    path('view_institution',views.view_institution,name='view_institution'),
    path('view_contributor',views.view_contributor,name='view_contributor'),
    path('approve_insti/<int:id>',views.approve_insti,name='approve_insti'),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)