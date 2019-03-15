from django.shortcuts import render
from core.models import Book
from django.views import generic

def books(request):
    """View function for the homepage of the site."""

    books = Book.objects.all()

    context = {
        'books': books,
    }    

    return render(request, 'core/index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10    
