from django.shortcuts import render, get_object_or_404 
from .models import Book
from django.http import Http404
# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {
        "books": books
    })


def book_page(request, id):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, pk=id)
    return render(request, 'book_outlet/book_page.html', {
        "title": book.title,
        "another": book.another,
        "reting": book.rating,
        "is_best_seller": book.is_best_seller
    })
