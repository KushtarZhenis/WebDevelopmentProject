from django.contrib import admin
from django.urls import path

from api.views import category_list, book_list, book, author_list, authormap_list

urlpatterns = [
    path('categories/', category_list),
    path('books/', book_list),
    path('book/<int:pk>/', book),
    path('authors/', author_list),
    path('authormap/', authormap_list),
]
