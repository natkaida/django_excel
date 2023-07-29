import yaml
from django.shortcuts import render

def student_list(request):
    with open('media/students.yaml', encoding='utf-8') as file:
        students = yaml.safe_load(file)
    return render(request, 'student_list.html', {'students': students})
