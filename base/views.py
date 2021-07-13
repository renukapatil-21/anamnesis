from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import add as ad
from django.contrib.auth.models import Group
from datetime import datetime
import random as r


def view(request):
    otp=""
    for i in range(4):
        otp+=str(r. randint(1,9))
        print ("Your One Time Password is ")
    var = {
        'otp' : otp
    }
        
    return render(request, 'base/view.html', var)


def doctor(request):
    if request.method == 'POST':
        members = ad.objects.all()
        return render(request, 'base/doctor2.html', {'members': members})
    else:
        return render(request, 'base/doctor.html')


def doctor2(request):
    members = ad.objects.all()
    return render(request, 'base/doctor2.html', {'members': members})

# Create your views here.
def index(request):
    # posts = Post.objects.all()
    # return render(request, 'blog/home.html', {'posts':posts})
    return render(request, 'base/home.html')

def dashboard(request):
    if request.user.is_authenticated:
        members = ad.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'base/dashboard.html',  {'full_name':full_name, 'groups':gps, 'members' : members})  
    else:
        return HttpResponseRedirect('/login/')

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation Your account has been!!!')
            user = form.save()
            # group =Group.objects.get(name='Author')
            # user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'base/signup.html', {'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully !!!')
                    return HttpResponseRedirect('/dashboard/')
        else:           
            form = LoginForm()
        return render(request, 'base/login.html', {'form':form}) 
    else:
        return HttpResponseRedirect('/dashboard/')    

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')                  


def add(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        user_gender = request.POST.get('user_gender')
        user_birthday = request.POST.get('user_birthday')
        user_phone = request.POST.get('user_phone')
        user_blood_group = request.POST.get('user_blood_group')
        user_allergy = request.POST.get('user_allergy')
        user_major_operation = request.POST.get('user_major_operation')
        add = ad(name = user_name, gender = user_gender, birth_date = user_birthday, phone = user_phone, blood_group = user_blood_group, allergy = user_allergy, major_operation = user_major_operation, date = datetime.today())
        add.save()
        messages.success(request, 'Your contact is submitted.')

    return render(request, 'base/add.html')


def share(request):
    return render(request, 'base/share.html')

def delete(request, id):
    instance = ad.objects.get(id = id)
    instance.delete()
    return render(request, 'base/dashboard.html')

def share(request, id):
    instance = ad.objects.get(id=id)
    instance.share()
    return render(request, 'base/dashboard.html')