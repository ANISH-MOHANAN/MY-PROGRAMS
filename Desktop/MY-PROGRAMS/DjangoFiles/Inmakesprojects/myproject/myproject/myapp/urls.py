from django.contrib import admin

from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('admin/',admin.site.urls),
    # path('operations/',views.operations,name='operations'),

]