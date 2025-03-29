"""
URL configuration for DigitalLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library.views import home, about, AuthorListView, BookListView, BookDetailView, GenreListView, GenreDetailView, \
    AuthorDetailView, AuthorFormView, CountryFormView, BookFormView, GenreFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),

    path('country/create/', CountryFormView.as_view(), name='country-create'),
    path('books/', GenreListView.as_view(), name='books'),
    #path('books/', BookListView.as_view(), name='books'),

    path('book/<int:pk>/', BookDetailView.as_view(), name='book'),
    path('book/create/', BookFormView.as_view(), name='book-create'),

    path('genres/', GenreListView.as_view(), name='genres'),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name='genre'),
    path('genre/create/', GenreFormView.as_view(), name='genre-create'),

    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author'),
    path('author/create/', AuthorFormView.as_view(), name='author-create'),
]
