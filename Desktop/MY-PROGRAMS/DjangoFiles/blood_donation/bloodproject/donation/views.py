from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def donation(request):
    if request.method == 'post':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        blood_group = request.POST['blood_group']
        email = request.POST['email']
        phone = request.POST['phone']
        disease = request.POST['disease']
        address = request.POST['address']
        user=User.objects.create_user(first_name=first_name,last_name=last_name,gender=gender,blood_group=blood_group,email=email,phone=phone,disease=disease,address=address)
        user.save();
        print("donation created")
        if user is not None:
            return redirect('/')
        else:
            messages.info(request,"Form is incomplete")
            return redirect("donation")
    return render(request,"donation.html")
