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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from DigitalLibrary import settings
from library.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accounts.views import SubmittableLoginView, logout_view, SingUpView
from library.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),

    path('country/create/', CountryFormView.as_view(), name='country-create'),
    path('books/', BookListView.as_view(), name='books'),

    path('book/<int:pk>/', BookDetailView.as_view(), name='book'),
    path('book/create/', BookCreateView.as_view(), name='book-create'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),

    path('genres/', GenreListView.as_view(), name='genres'),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name='genre'),
    path('genre/create/', GenreFormView.as_view(), name='genre-create'),
    path('genre/add/', GenrePopupCreateView.as_view(), name='genre-add'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author'),
    #path('author/create/', AuthorFormView.as_view(), name='author-create'),
    path('author/create/', AuthorCreateView.as_view(), name='author-create'),
    path('author/add/', AuthorPopupCreateView.as_view(), name='author-add'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    path('author/delete/<int:pk>/', AuthorDeleteView.as_view(), name='author-delete'),
    path('search/', search, name='search'),
    path('author/create/', AuthorCreateView.as_view(), name='author-create'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    path('author/delete/<int:pk>/', AuthorDeleteView.as_view(), name='author-delete'),
    path('search/', search, name='search'),

    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    # --- můžeme odstranit ---
    #path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', SingUpView.as_view(), name='signup'),
    path('image/create/', ImageCreateView.as_view(), name='image-create'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
