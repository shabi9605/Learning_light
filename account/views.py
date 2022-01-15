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


def index(request):
    payment_count=Payment.objects.filter(is_paid=True).count()
    donation_count=ValuableDonation.objects.all().count()
    return render(request,'index.html',{'payment_count':payment_count,'donation_count':donation_count})



def institution_register(request):
    reg=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        institution_form=InstitutionForm(data=request.POST)
        if user_form.is_valid() and institution_form.is_valid():
            user=user_form.save()
            user.save()
            profile=institution_form.save(commit=False)
            profile.user=user
            profile.save()

            reg=True
            return redirect('user_login')
        else:
            HttpResponse("invalid form")
    else:
         user_form=UserForm()
         institution_form=InstitutionForm()
    return render(request,'institution_register.html',{'register':reg,'user_form':user_form,'institution_form':institution_form}) 



def student_register(request):
    reg=False
    if request.method=='POST':
        user_form=UserForm(request.POST)
        student_form=StudentForm(request.POST,request.FILES)
        if user_form.is_valid() and student_form.is_valid():
            user=user_form.save()
            user.save()
            profile=student_form.save(commit=False)
            profile.user=user
            profile.save()

            reg=True
            return redirect('user_login')
        else:
            HttpResponse("invalid form")
    else:
         user_form=UserForm()
         student_form=StudentForm()
    return render(request,'student_register.html',{'register':reg,'user_form':user_form,'student_form':student_form})



def contributor_register(request):
    reg=False
    if request.method=='POST':
        user_form=UserForm(request.POST)
        contributor_form=ContributorForm(request.POST,request.FILES)
        if user_form.is_valid() and contributor_form.is_valid():
            user=user_form.save()
            user.save()
            profile=contributor_form.save(commit=False)
            profile.user=user
            profile.save()

            reg=True
            return redirect('user_login')
        else:
            HttpResponse("invalid form")
    else:
         user_form=UserForm()
         contributor_form=ContributorForm()
    return render(request,'contributor_register.html',{'register':reg,'user_form':user_form,'contributor_form':contributor_form})




def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        try:
            user1=Institution.objects.get(user=user)
        except:
            pass
            
        try:
            user2=Student.objects.get(user=user)
        except:
            pass

        try:
            user3=Contributor.objects.get(user=user)
        except:
            pass

        

        if user:
            if user.is_active:
                try:
                    if user1:
                        active=Institution.objects.all().filter(user_id=user.id,status=True)
                        if active:
                            login(request,user)
                
                
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            messages.success(request,f'Waiting for approval')
                            return redirect('user_login')
                except:
                    pass

                try:
                    if user2:
                        active=Student.objects.all().filter(user_id=user.id,status=True)
                        if active:
                            login(request,user)
                
                
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            messages.success(request,f'Waiting for approval')
                            return redirect('user_login')
                except:
                    pass

                try:
                    if user3:
                        
                        login(request,user)
                
                
                        return HttpResponseRedirect(reverse('contributordashboard'))
                    else:
                        messages.success(request,f'Waiting for approval')
                        return redirect('user_login')
                except:
                    pass

                try:
                    if user.is_superuser:
                        
                        login(request,user)
                
                
                        return HttpResponseRedirect(reverse('dashboard'))
                    else:
                        messages.success(request,f'Waiting for approval')
                        return redirect('user_login')
                except:
                    pass

                
            else:
                return HttpResponse("Not active")
        else:
            return HttpResponse("Invalid username or password")
    else:
        
        return render(request,'login.html')



def contributordashboard(request):
    return render(request,'contributor_dashboard.html')


def view_request(request):
    requests=Request.objects.all().order_by('-date')
    return render(request,'view_request.html',{'requests':requests})



def dashboard(request):
    user=request.user
    print(user)
    try:
        user1=Institution.objects.get(user=user)
        return render(request,'dashboard.html',{"qs":user1})
    except:
        pass
            
    try:
        user2=Student.objects.get(user=user)
        return render(request,'dashboard.html',{"qs":user2})
    except:
        pass
    return render(request,'dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


def profile(request):
    user=request.user
    try:
        user1=Institution.objects.get(user=user)
        return render(request,'profile.html',{"qs":user1})
    except:
        pass
            
    try:
        user2=Student.objects.get(user=user)
        return render(request,'profile.html',{"qs":user2})
    except:
        pass

    try:
        user3=Contributor.objects.get(user=user)
        return render(request,'c_profile.html',{"qs":user3})
    except:
        pass
    return render(request,'profile.html')



def request_add(request):
    
    if request.method=="POST":
        request_form=RequestForm(request.POST)
        if request_form.is_valid():
            cp=Request(user=request.user,request=request_form.cleaned_data['request'],number=request_form.cleaned_data['number'],phone=request_form.cleaned_data['phone'])
            cp.save()

            
            return render(request,'request_form.html',{'msg':'successfully added request'})
        else:
            return HttpResponse("Invalid form")
    request_form=RequestForm()
    return render(request,'request_form.html',{'form':request_form})


def request(request):
    acc_request=Request.objects.filter(user=request.user).order_by('-date')
    return render(request,'accepted_request.html',{'request':acc_request})






def donation_history(request):
    donation=Payment.objects.filter(user=request.user).order_by('-date')
    return render(request,'history.html',{'history':donation})





def view_our_students(request):
    students=Student.objects.filter(institution=request.user.institution)
    print(students)
    return render(request,'view_students.html',{'students':students})




def approve_student(request,id):
    schema=Student.objects.get(id=id)
    print(schema)
    update_schema_form=ApprovestudentForm(instance=schema)
    if request.method=="POST":
        update_schema_form=ApprovestudentForm(request.POST,request.FILES,instance=schema)
        update_schema_form.save()
        return redirect('view_our_students')
    return render(request,'student_approve.html',{'form':update_schema_form})



def view_institution(request):
    institution=Institution.objects.all().order_by('-id')
    return render(request,'view_institution.html',{'institution':institution})



def view_contributor(request):
    contrib=Contributor.objects.all().order_by('-id')
    return render(request,'view_contributor.html',{'contrib':contrib})



def approve_insti(request,id):
    schema=Institution.objects.get(id=id)
    print(schema)
    update_schema_form=ApproveInstitution(instance=schema)
    if request.method=="POST":
        update_schema_form=ApproveInstitution(request.POST,request.FILES,instance=schema)
        update_schema_form.save()
        return redirect('view_institution')
    return render(request,'student_approve.html',{'form':update_schema_form})
