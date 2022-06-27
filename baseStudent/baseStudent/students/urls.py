from django.contrib import admin
from django.urls import path

from students.views import MyViwe_1, MyViwe_2, MyViwe_3, MyViwe_4

urlpatterns = [    
    path('viwe/', MyViwe_1.as_view()),
    path('viwe/<pk>', MyViwe_2.as_view()),    
    path('subject/', MyViwe_3.as_view()),
    path('subject/<pk>/', MyViwe_4.as_view())
]