from django.test import TestCase
from library.models import *

class ModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        book = Book.objects.create(
            title_orig="Original title",
            title_cz="Cz name",
            ISBN="1234567890123",
            language="English",
            number_of_pages=312,
            format="Hard",
            year_published=1999,
            publisher="Original publisher",
            description="Original description",
            book_type="Novel",
            weight=321,
        )

        book2 = Book.objects.create(
            title_orig="Nonoriginal title",
        )

        book3 = Book.objects.create(
            title_orig="Nonoriginal title",
            year_published=2100,
        )

        book4 = Book.objects.create(
            title_cz="Original CZ title",
        )

        genre_scifi = Genre.objects.create(
            name="Sci-Fi"
        )
        genre_comedy = Genre.objects.create(
            name="Comedy"
        )
        book.genres.add(genre_scifi)
        book.genres.add(genre_comedy)

        country_czechia = Country.objects.create(
            name="Czech republic",
        )
        country_slovakia = Country.objects.create(
            name="Slovakia",
        )


        author = Author.objects.create(
            first_name="Honza",
            surname="Pepan",
            date_of_birth=date(1999, 12, 31),
            date_of_death=date(2025, 4, 6),
            country=country_czechia,
            biography="alksjdfhjk.lasdflk"
        )

        book.authors.add(author)

        book.save()

    def setUp(self):
        print('-'*80)

    def test_title_orig(self):
        book = Book.objects.get(id=1)
        print(f'test_title_orig: "{book.title_orig}"')
        self.assertEqual(book.title_orig, "Original title")

    def test_book_str(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.__str__(), "Original title (1999)")
        book2 = Book.objects.get(id=2)
        self.assertEqual(book2.__str__(), "Nonoriginal title")
        book3 = Book.objects.get(id=3)
        print(f'test_book_str: "{book3.__str__()}"')
        #test passed because no limit in model.py to Book/year_published, this is
        #solved in forms.py in clean_year_published - limit set to 2100, over creates
        #validation error, year set to 2100 in case of future releases
        self.assertEqual(book3.__str__(), "Nonoriginal title (2100)")
        book4 = Book.objects.get(id=4)
        self.assertEqual(book4.__str__(), "")

    # def test_create_book_with_minimal_fields(self):
    #     book = Book.objects.get(id=2)
    #     self.assertEqual(book.title_orig, "Nonoriginal title")
    #     self.assertEqual(str(book), "Nonoriginal title")
    #     self.assertEqual(repr(book), "Nonoriginal title")
    #     self.assertEqual(book.genres.count(), 1)
    #     self.assertEqual(book.authors.count(), 0)

