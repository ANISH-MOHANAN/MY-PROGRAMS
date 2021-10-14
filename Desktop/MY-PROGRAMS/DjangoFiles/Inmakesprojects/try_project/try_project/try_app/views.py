from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def new_fun(requests):
    return HttpResponse("this is my second experiment and iam feeling better")
