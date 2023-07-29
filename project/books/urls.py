from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.all_books, name='all_books'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('programming/', views.programming, name='programming'),
    path('thriller/', views.thriller, name='thriller'),
    path('mystery/', views.mystery, name='mystery'),
    path('fantasy/', views.fantasy, name='fantasy'),
]