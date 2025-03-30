from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView, CreateView, UpdateView, DeleteView

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
            descrption=cleaned_data['description'],
            book_type=cleaned_data['book_type'],
            weight=cleaned_data['weight'],
            cover=cleaned_data['cover'],
        )
        return result

    def form_invalid(self, form):
        print("Ej bistu, ogrcal si mi krpce")
        return super().form_invalid(form)

class BookCreateView(CreateView):
    template_name = 'form.html'
    form_class = BookModelForm
    success_url = reverse_lazy('books') #maybe 'books'?

    def form_invalid(self, form):
        print("Form 'BookModelForm' is invalid")
        return super().form_invalid(form)

class BookUpdateView(UpdateView):
    template_name = "form.html"
    form_class = BookModelForm
    success_url = reverse_lazy('books')
    model = Author

    def form_invalid(self, form):
        print("Form 'AuthorModelForm' is invalid")
        return super().form_invalid(form)

class BookDeleteView(DeleteView):
    template_name = "confirm_delete.html"
    model = Book
    success_url = reverse_lazy('books')
class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'author.html'

class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'authors.html'

""" !!!delete afterwards!!!
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
"""

class AuthorCreateView(CreateView):
    template_name = 'form.html'
    form_class = AuthorModelForm
    success_url = reverse_lazy('authors')

    def form_invalid(self, form):
        print("Form 'AuthorModelForm' is invalid")
        return super().form_invalid(form)

class AuthorUpdateView(UpdateView):
    template_name = "form.html"
    form_class = AuthorModelForm
    success_url = reverse_lazy('authors')
    model = Author

    def form_invalid(self, form):
        print("Form 'AuthorModelForm' is invalid")
        return super().form_invalid(form)

class AuthorDeleteView(DeleteView):
    template_name = "confirm_delete.html"
    model = Author
    success_url = reverse_lazy('authors')

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
    success_url = reverse_lazy('books')

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

# class GenreCreateView(CreateView):
#     template_name = 'form.html'
#     form_class = GenreModelForm
#     success_url = reverse_lazy('genres') #maybe 'books'?
#
#     def form_invalid(self, form):
#         print("Form 'GenreModelForm' is invalid")
#         return super().form_invalid(form)
#
# class GenreUpdateView(UpdateView):
#     template_name = "form.html"
#     form_class = GenreModelForm
#     success_url = reverse_lazy('genres')
#     model = Author
#
#     def form_invalid(self, form):
#         print("Form 'AuthorModelForm' is invalid")
#         return super().form_invalid(form)
#
# class GenreDeleteView(DeleteView):
#     template_name = "confirm_delete.html"
#     model = Author
#     success_url = reverse_lazy('genres')

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

