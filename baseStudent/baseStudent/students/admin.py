from tkinter import S
from django.contrib import admin
from students.models import Student, StudentGroup, Sabject


admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(Sabject)

# Register your models here.
