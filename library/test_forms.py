from django.test import TestCase
from library.forms import *
from library.models import *

class AuthorModelFormTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Italy")

    def test_valid_author_form(self):
        form = AuthorModelForm(data={
            'first_name': 'giovanni',
            'surname': 'boccaccio',
            'country': self.country.id
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['first_name'], 'Giovanni')
        self.assertEqual(form.cleaned_data['surname'], 'Boccaccio')

    def test_invalid_author_form_missing_names(self):
        form = AuthorModelForm(data={'first_name': '', 'surname': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('Please enter both initial_name and initial_surname', str(form.errors))


class BookModelFormTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Drama")

    def test_valid_book_form(self):
        form = BookModelForm(data={
            'title_orig': 'hamlet',
            'genres': [self.genre.id],
            'number_of_pages': 300,
            'year_published': 1603,
            'publisher': 'penguin books',
            'description': 'a tragic play'
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['title_orig'], 'Hamlet')
        self.assertEqual(form.cleaned_data['publisher'], 'Penguin books')
        self.assertEqual(form.cleaned_data['description'], 'A tragic play')

    def test_invalid_book_form_year(self):
        form = BookModelForm(data={
            'title_orig': 'future book',
            'genres': [self.genre.id],
            'year_published': 9999
        })
        self.assertFalse(form.is_valid())
        self.assertIn("Insert correct year", str(form.errors))


class GenreModelFormTest(TestCase):
    def test_genre_name_capitalize(self):
        form = GenreModelForm(data={'name': 'romance'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['name'], 'Romance')


class CountryModelFormTest(TestCase):
    def test_country_name_capitalize(self):
        form = CountryModelForm(data={'name': 'greece'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['name'], 'Greece')