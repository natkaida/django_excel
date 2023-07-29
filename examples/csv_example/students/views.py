import csv
from django.shortcuts import render

def student_list(request):
    students = []
    with open('media/students.csv', 'r', encoding='utf-8') as file:
        csv_data = csv.DictReader(file)
        for row in csv_data:
            students.append(row)
    return render(request, 'student_list.html', {'students': students})
