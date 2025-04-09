from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.utils.html import escapejs
from django.views.generic import DetailView, ListView, FormView, CreateView, UpdateView, DeleteView
from django_addanother.widgets import AddAnotherWidgetWrapper
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView, CreateView, UpdateView, DeleteView
from django_addanother.widgets import AddAnotherWidgetWrapper

from DigitalLibrary.settings import DEBUG
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

    def form_invalid(self, form):
        print("Form 'BookModelForm' is invalid")
        return super().form_invalid(form)

class BookCreateView(PermissionRequiredMixin,CreateView):
    template_name = 'form.html'
    form_class = BookModelForm
    success_url = reverse_lazy('books') #maybe 'books'?
    permission_required = 'library.add_book'

    def form_valid(self, form):
        if DEBUG:
            print("Book form is valid")
        return super().form_valid(form)

    def form_invalid(self, form):
        if DEBUG:
            print("Form 'BookModelForm' is invalid")
        return super().form_invalid(form)

class BookUpdateView(PermissionRequiredMixin,UpdateView):
    template_name = "form.html"
    form_class = BookModelForm
    success_url = reverse_lazy('books')
    model = Book
    permission_required = 'library.change_book'

    def form_invalid(self, form):
        if DEBUG:
            print("Form 'BookModelForm' is invalid")
        return super().form_invalid(form)

class BookDeleteView(PermissionRequiredMixin,DeleteView):
    template_name = "confirm_delete.html"
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'library.delete_book'

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

class AuthorCreateView(PermissionRequiredMixin,CreateView):
    template_name = 'form.html'
    form_class = AuthorModelForm
    success_url = reverse_lazy('authors')
    permission_required = 'library.add_author'


    def form_invalid(self, form):
        print("Form 'AuthorModelForm' is invalid")
        return super().form_invalid(form)

class AuthorPopupCreateView(PermissionRequiredMixin,CreateView):
    model = Author
    template_name = 'author_form_popup.html'
    form_class = AuthorModelForm
    success_url = reverse_lazy('author-add')

    def form_valid(self, form):
        self.object = form.save()

        new_id = self.object.pk
        new_label = str(self.object)

        return HttpResponse(
            f'<script>window.opener.dismissAddAnotherPopup(window, "{escapejs(new_id)}", "{escapejs(new_label)}");</script>',
            content_type='text/html'
        )

class AuthorUpdateView(PermissionRequiredMixin,UpdateView):
    template_name = "form.html"
    form_class = AuthorModelForm
    success_url = reverse_lazy('authors')
    model = Author
    permission_required = 'library.change_author'

    def form_invalid(self, form):
        print("Form 'AuthorModelForm' is invalid")
        return super().form_invalid(form)

class AuthorDeleteView(PermissionRequiredMixin,DeleteView):
    template_name = "confirm_delete.html"
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'library.delete_author'

class GenreDetailView(DetailView):
    model = Genre
    context_object_name = 'genre'
    template_name = 'genre.html'

class GenreListView(ListView):
    model = Genre
    context_object_name = 'genres'
    template_name = 'genres.html'

class GenreFormView(LoginRequiredMixin,FormView):
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

class GenrePopupCreateView(LoginRequiredMixin,CreateView):
    model = Genre
    template_name = 'genre_form_popup.html'
    form_class = GenreModelForm
    success_url = reverse_lazy('genre-add')

    def form_valid(self, form):
        self.object = form.save()

        new_id = self.object.pk
        new_label = str(self.object)

        return HttpResponse(
            f'<script>window.opener.dismissAddAnotherPopup(window, "{escapejs(new_id)}", "{escapejs(new_label)}");</script>',
            content_type='text/html'
        )

# class GenreCreateView(CreateView):
#     template_name = 'form.html'
#     form_class = GenreModelForm
#     success_url = reverse_lazy('genres') #maybe 'books'?
#
#     def form_invalid(self, form):
#        if DEBUG:
#         print("Form 'GenreModelForm' is invalid")
#        return super().form_invalid(form)
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

class CountryFormView(LoginRequiredMixin,FormView):
    form_class = CountryModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('genres')

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

def search(request):
    if request.method == 'POST':
        search_string = request.POST.get('search').strip()
        if len(search_string) > 0:
            books_title_orig = Book.objects.filter(title_orig__contains=search_string)
            authors_first_name = Author.objects.filter(first_name__contains=search_string)

            context = {'search': search_string,
                       'books_title_orig': books_title_orig,
                       'authors_first_name': authors_first_name
                       }
            return render(request, 'search.html', context)
    return render(request, 'home.html')