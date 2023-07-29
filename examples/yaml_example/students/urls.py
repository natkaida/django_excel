from django.urls import path
from students.views import student_list

urlpatterns = [
    path('students/', student_list, name='student_list'),
]