from django.shortcuts import render
from core.models import Book
from django.views import generic

def index(request):
    """View function for the homepage of the site."""

    books = Book.objects.all()

    context = {
        'books': books,
    }    

    return render(request, 'core/index.html', context=context)
