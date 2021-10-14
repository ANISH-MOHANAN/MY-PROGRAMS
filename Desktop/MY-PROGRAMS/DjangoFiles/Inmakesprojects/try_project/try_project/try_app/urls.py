
from django.urls import path
from try_app import views

urlpatterns = [
    path('',views.new_fun,name='new_fun')
]
