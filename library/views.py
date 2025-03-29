from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView

from library.forms import AuthorModelForm, BookModelForm, GenreModelForm, CountryModelForm
from library.models import Book, Author, Genre, Country


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

class BookFormView(FormView):
    form_class = BookModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Book.objects.create(
            title_orig=cleaned_data['title_orig'],
            title_cz=cleaned_data['title_cz'],
            authors=cleaned_data['authors'],
            ISBN=cleaned_data['ISBN'],
            genres=cleaned_data['genres'],
            language=cleaned_data['language'],
            number_of_pages=cleaned_data['number_of_pages'],
            format=cleaned_data['format'],
            year_published=cleaned_data['year_published'],
            publisher=cleaned_data['publisher'],
            descrption=cleaned_data['descrption'],
            book_type=cleaned_data['book_type'],
            weight=cleaned_data['weight'],
            cover=cleaned_data['cover'],
        )
        return result

    def form_invalid(self, form):
        print("Ej bistu, ogrcal si mi krpce")
        return super().form_invalid(form)

class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'author.html'

class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'authors.html'

class AuthorFormView(FormView):
    form_class = AuthorModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('authors')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Author.objects.create(
            first_name=cleaned_data['first_name'],
            surname=cleaned_data['surname'],
            date_of_birth=cleaned_data['date_of_birth'],
            date_of_death=cleaned_data['date_of_death'],
            country=cleaned_data['country'],
            biography=cleaned_data['biography'],
        )
        return result

    def form_invalid(self, form):
        print("Ej bistu, ogrcal si mi krpce")
        return super().form_invalid(form)

class GenreDetailView(DetailView):
    model = Genre
    context_object_name = 'genre'
    template_name = 'genre.html'

class GenreListView(ListView):
    model = Genre
    context_object_name = 'genres'
    template_name = 'genres.html'

class GenreFormView(FormView):
    form_class = GenreModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('genres')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Genre.objects.create(
            name=cleaned_data['name'],
        )
        return result

    def form_invalid(self, form):
        print("Ej bistu, ogrcal si mi krpce")
        return super().form_invalid(form)

class CountryFormView(FormView):
    form_class = CountryModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('countries')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Country.objects.create(
            name=cleaned_data['name'],
        )
        return result

    def form_invalid(self, form):
        print("Ej bistu, ogrcal si mi krpce")
        return super().form_invalid(form)
