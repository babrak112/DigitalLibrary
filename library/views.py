from django.shortcuts import render
from django.views.generic import DetailView, ListView

from library.models import Book, Author


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book.html'

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books.html'


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'author.html'

class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'authors.html'






