from django.contrib import admin

from library.models import Book, Author, Country, Genre

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Country)
admin.site.register(Genre)


