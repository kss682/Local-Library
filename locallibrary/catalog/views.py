from django.shortcuts import render
from django.views import generic
from catalog.models import Book,Author,Genre
# Create your views here.
def index(request):
    return render(request,'index.html',{})

class BooklistView(generic.ListView):
    model = Book
    template_name = 'books.html'

class AuthorlistView(generic.ListView):
    model = Author
    template_name = 'authors.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author-details.html'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book-details.html'