from django.shortcuts import render
from openpyxl import load_workbook

def all_books(request):
    file_path = 'media/books.xlsx'
    workbook = load_workbook(filename=file_path)
    worksheet = workbook.active

    books = []
    skip_first_row = True
    for row in worksheet.iter_rows(values_only=True, min_row=2 if skip_first_row else 1):
        book = {
            'book_id': int(row[0]),
            'title': row[1],
            'author': row[2],
            'genre': row[3],
            'year': int(row[4]),
            'description': row[5],
            'cover': row[6]
        }
        books.append(book)

    return render(request, 'books.html', {'books': books})

def book_detail(request, book_id):
    file_path = 'media/books.xlsx'
    workbook = load_workbook(filename=file_path)
    worksheet = workbook.active

    books = []
    skip_first_row = True
    for row in worksheet.iter_rows(values_only=True, min_row=2 if skip_first_row else 1):
        book = {
            'book_id': int(row[0]),
            'title': row[1],
            'author': row[2],
            'genre': row[3],
            'year': int(row[4]),
            'description': row[5],
            'cover': row[6]
        }
        books.append(book)

    book = books[int(book_id) - 1]  # Получение данных об отдельной книге по ее индексу

    return render(request, 'book_detail.html', {'book': book})

def thriller(request):
    file_path = 'media/books.xlsx'
    workbook = load_workbook(filename=file_path)
    worksheet = workbook.active

    books = []
    skip_first_row = True
    for row in worksheet.iter_rows(values_only=True, min_row=2 if skip_first_row else 1):
        genre = row[3]
        if genre.lower() == 'триллер':
            book = {
                'book_id': int(row[0]),            
                'title': row[1],
                'author': row[2],
                'genre': genre,
                'year': int(row[4]),
                'description': row[5],
                'cover': row[6]
            }
            books.append(book)

    return render(request, 'books.html', {'books': books})

def mystery(request):
    file_path = 'media/books.xlsx'
    workbook = load_workbook(filename=file_path)
    worksheet = workbook.active

    books = []
    skip_first_row = True
    for row in worksheet.iter_rows(values_only=True, min_row=2 if skip_first_row else 1):
        genre = row[3]
        if genre.lower() == 'детектив':
            book = {
                'book_id': int(row[0]),            
                'title': row[1],
                'author': row[2],
                'genre': genre,
                'year': int(row[4]),
                'description': row[5],
                'cover': row[6]
            }
            books.append(book)
    return render(request, 'books.html', {'books': books})

def fantasy(request):
    file_path = 'media/books.xlsx'
    workbook = load_workbook(filename=file_path)
    worksheet = workbook.active

    books = []
    skip_first_row = True
    for row in worksheet.iter_rows(values_only=True, min_row=2 if skip_first_row else 1):
        genre = row[3]
        if genre.lower() == 'фэнтези':
            book = {
                'book_id': int(row[0]),            
                'title': row[1],
                'author': row[2],
                'genre': genre,
                'year': int(row[4]),
                'description': row[5],
                'cover': row[6]
            }
            books.append(book)

    return render(request, 'books.html', {'books': books})

def programming(request):
    file_path = 'media/books.xlsx'
    workbook = load_workbook(filename=file_path)
    worksheet = workbook.active

    books = []
    skip_first_row = True
    for row in worksheet.iter_rows(values_only=True, min_row=2 if skip_first_row else 1):
        genre = row[3]
        if genre.lower() == 'программирование':
            book = {
                'book_id': int(row[0]),            
                'title': row[1],
                'author': row[2],
                'genre': genre,
                'year': int(row[4]),
                'description': row[5],
                'cover': row[6]
            }
            books.append(book)

    return render(request, 'books.html', {'books': books})
