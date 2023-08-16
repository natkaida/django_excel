from django.shortcuts import render
from openpyxl import load_workbook

file_path = 'media/books.xlsx'
workbook = load_workbook(filename=file_path)
WORKSHEET = workbook.active


def get_book_dict(row):
    book = {
        'book_id': int(row[0]),
        'title': row[1],
        'author': row[2],
        'genre': row[3],
        'year': int(row[4]),
        'description': row[5],
        'cover': row[6]
    }
    return book


def get_books(genre: str = None):
    books = []
    skip_first_row = True
    for row in WORKSHEET.iter_rows(values_only=True, min_row=2 if skip_first_row else 1):
        if not genre:
            books.append(get_book_dict(row))
        elif genre.lower() == row[3].lower():
            books.append(get_book_dict(row))
    return books


def all_books(request):
    books = get_books()
    return render(request, 'books.html', {'books': books})


def book_detail(request, book_id: int):
    books = get_books()
    book = books[int(book_id) - 1]
    return render(request, 'book_detail.html', {'book': book})


def thriller(request):
    books = get_books(genre='триллер')
    return render(request, 'books.html', {'books': books})


def mystery(request):
    books = get_books(genre='детектив')
    return render(request, 'books.html', {'books': books})


def fantasy(request):
    books = get_books(genre='фэнтези')
    return render(request, 'books.html', {'books': books})


def programming(request):
    books = get_books(genre='программирование')
    return render(request, 'books.html', {'books': books})
