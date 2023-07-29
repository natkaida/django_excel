import json
from django.shortcuts import render

def student_list(request):
    with open('media/students.json', 'r', encoding='utf-8') as file:
        students = json.load(file)
    return render(request, 'student_list.html', {'students': students})