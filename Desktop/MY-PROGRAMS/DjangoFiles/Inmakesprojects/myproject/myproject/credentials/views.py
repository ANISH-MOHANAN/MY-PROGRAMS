import django as django
from django.contrib import messages, auth
from django.contrib.auth.models import AbstractUser, User
from django.shortcuts import render, redirect

django.contrib.auth.models.User(AbstractUser)

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password1']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return  redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return  redirect('registration')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)

            user.save();
            print("user created")
            return redirect('login')

        else:
            messages.info(request,'password not matching')
            return redirect('registration')
        return redirect('/')
    return render(request,"registration.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
