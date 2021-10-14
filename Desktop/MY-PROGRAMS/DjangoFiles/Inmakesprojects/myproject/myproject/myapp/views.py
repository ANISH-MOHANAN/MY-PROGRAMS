from django.http import HttpResponse
from django.shortcuts import render
from . models import our_services
from . models import why_choos_us
# Create your views here.
def demo(request):
    obj=our_services.objects.all()
    key=why_choos_us.objects.all()
    return render(request,"index.html",{'result':obj,'res':key})


# def operations(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,"result.html",{'result1':add,'result2':sub,'result3':mul,'result4':div})