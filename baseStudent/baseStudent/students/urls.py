from django.contrib import admin
from django.urls import path

from students.views import MyViwe

urlpatterns = [    
    path('viwe/<pk>', MyViwe.as_view())
]