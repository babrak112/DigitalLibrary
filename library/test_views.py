from django.test import TestCase
from django.urls import reverse

from library.models import *

class BookViewTests(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Fantasy")
        self.book = Book.objects.create(
            title_orig="The Hobbit",
            number_of_pages=310,
            year_published=1937
        )
        self.book.genres.add(self.genre)

    def test_book_list_view(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.book, response.context['books'])

    def test_book_update_view(self):
        response = self.client.post(reverse('book-update', args=[self.book.pk]), {
            'title_orig': 'The Hobbit: Revised',
            'genres': [self.genre.id],
            'number_of_pages': 320,
            'year_published': 1937
        })
        self.assertEqual(response.status_code, 302)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title_orig, "The Hobbit")