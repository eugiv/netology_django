from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book
from django.urls import reverse


def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {'books': books}
    return render(request, template, context)


def choosen_book(request, book_date):
    books_dates_all = Book.objects.values_list('pub_date').distinct()
    unique_dates = [date[0] for date in books_dates_all]
    book_filtered = Book.objects.filter(pub_date=book_date)

    paginator = Paginator(unique_dates, 10)
    page = paginator.get_page(unique_dates)

    template = 'books/books_list.html'
    context = {'books': book_filtered, 'page': page}
    return render(request, template, context)
