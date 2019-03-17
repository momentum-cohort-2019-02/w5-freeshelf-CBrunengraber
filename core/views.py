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

def book_detail_view(request, slug):
    books = get_object_or_404(Event, slug=slug)
    return render(request, "core/book_detail.html", {"books": books})