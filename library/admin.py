from django.contrib import admin

from library.models import Book, Author, Country, Genre, Image

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Image)


