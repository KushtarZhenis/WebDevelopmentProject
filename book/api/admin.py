from django.contrib import admin
from api.models import Category, Book, Author, Authormap

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Authormap)
