from django.forms import ModelForm

from library.models import Country, Author, Genre, Book


class AuthorModelForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class GenreModelForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class CountryModelForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'