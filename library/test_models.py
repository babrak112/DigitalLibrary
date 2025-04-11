from django.test import TestCase
from library.models import *

class GenreModelTest(TestCase):
    def test_genre_str_and_repr(self):
        genre = Genre.objects.create(name="Mystery")
        self.assertEqual(str(genre), "Mystery")
        self.assertEqual(repr(genre), "Genre(name=Mystery)")


class CountryModelTest(TestCase):
    def test_country_str_and_repr(self):
        country = Country.objects.create(name="France")
        self.assertEqual(str(country), "France")
        self.assertEqual(repr(country), "Country(name=France)")


class AuthorModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Sweden")

    def test_author_str_with_dob(self):
        author = Author.objects.create(
            first_name="Astrid",
            surname="Lindgren",
            date_of_birth=date(1907, 11, 14),
            country=self.country
        )
        self.assertEqual(str(author), "Astrid Lindgren (1907-11-14)")
        self.assertEqual(repr(author), "Author(first_name=Astrid, surname=Lindgren)")

    def test_author_str_without_dob(self):
        author = Author.objects.create(
            first_name="Erik",
            surname="Larsson",
            country=self.country
        )
        self.assertEqual(str(author), "Erik Larsson")

    def test_date_of_birth_eu_format(self):
        author = Author.objects.create(date_of_birth=date(1950, 4, 9))
        self.assertEqual(author.date_of_birth_eu(), "09. 04. 1950")


class BookModelTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Adventure")

    def test_book_str_and_repr(self):
        book = Book.objects.create(title_orig="Robinson Crusoe", year_published=1719)
        book.genres.add(self.genre)
        self.assertEqual(str(book), "Robinson Crusoe (1719)")
        self.assertEqual(repr(book), "Book(Robinson Crusoe)")
