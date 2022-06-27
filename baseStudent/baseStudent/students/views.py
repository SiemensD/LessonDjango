from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from students.models import Student, Subject

class MyViwe_1(View):
    def get(self, request):
        name = request.GET.get('name', False)

        students = Student.objects.all()
        if name:
            students=students.filter(name=name)

        students_data = []
        for student in students:
            students_data.append({'name':student.name})
        return JsonResponse({'data':students_data})

    def post(self, request):

        name = request.POST.get('name', '')
        students=Student.filter(name=name)
        return HttpResponse(name)

class MyViwe_2(View):
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            students_data = {'name':student.name}
        except Student.DoesNotExist:
            students_data = {}

        return JsonResponse({'data':students_data})

class MyViwe_3(View):
    def get(self, request):
        name = request.GET.get('name', False)

        subjects = Subject.objects.all()
        if name:
            subjects=subjects.filter(name=name)

        subjects_data = []
        for subject in subjects:
            subjects_data.append({'name':subject.name})
        return JsonResponse({'data':subjects_data})

class MyViwe_4(View):
    def get(self, request, pk):
        try:
            subject = Subject.objects.get(pk=pk)
            subjects_data = {'name':subject.name}
        except Subject.DoesNotExist:
            subjects_data = {}

        return JsonResponse({'data':subjects_data})


