from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def students(request):
    return render(request, 'students_home.html')


def about(request):
    return render(request, 'about_students.html')
