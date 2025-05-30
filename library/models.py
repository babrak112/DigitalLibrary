from django.db.models import *


class Genre(Model):
    name = CharField(max_length=45, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Genre(name={self.name})"

    def __str__(self):
        return f"{self.name}"

class Author(Model):
    first_name = CharField(max_length=45, null=True, blank=True)
    surname = CharField(max_length=45, null=True, blank=True)
    date_of_birth = DateField(null=True, blank=True)
    date_of_death = DateField(null=True, blank=True)
    country = ForeignKey("Country", null=True, blank=True, on_delete=SET_NULL, related_name='authors')
    biography = TextField(null=True, blank=True)


class Book(Model):
    title_orig = CharField(max_length=100,null=False, blank=False)
    title_cz = CharField(max_length=100,null=True, blank=True)
    authors = ManyToManyField(Author,max_length=45,blank=True, related_name='books')
    ISBN = CharField(max_length=20,null=True, blank=True)
    genres = ManyToManyField(Genre,max_length=45,blank=True, related_name='books')
    language = CharField(max_length=45,null=True, blank=True)
    number_of_pages = CharField(max_length=45,null=True, blank=True)
    format = CharField(max_length=10,null=True, blank=True)
    year_published = IntegerField(null=True, blank=True)
    publisher = CharField(max_length=45,null=True, blank=True)
    description = TextField(null=True, blank=True)
    book_type = CharField(max_length=45,null=True, blank=True)
    weight = IntegerField(null=True, blank=True)
    cover = CharField(max_length=45,null=True, blank=True)

    class Meta:
        ordering = ['title_orig']

    def __repr__(self):
        return f"Book({self.title_orig})"

    def __str__(self):
        return f"{self.title_orig} ({self.year_published})"




class Country(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Countries"

    def __repr__(self):
        return f"Country(name={self.name})"

    def __str__(self):
        return f"{self.name}"
