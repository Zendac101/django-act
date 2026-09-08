from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students'),
    path('about/', views.about, name='about')
]
