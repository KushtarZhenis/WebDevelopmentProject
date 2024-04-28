from django.db import models
from django.core.serializers import serialize


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"ID: {self.id}, Name: {self.title}"

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
        }

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnailUrl = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    rateCount = models.IntegerField(default=0)
    totalRate = models.IntegerField(default=0)
    isFree = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}"

    def get_authors(self):
        author_maps = Authormap.objects.filter(bookId=self.id)
        author_ids = author_maps.values_list('authorId', flat=True)
        authors = Author.objects.filter(id__in=author_ids)
        author_list = [author.name for author in authors]
        return author_list

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'thumbnailUrl': self.thumbnailUrl,
            'url': self.url,
            'rateCount': self.rateCount,
            'totalRate': self.totalRate,
            'isFree': self.isFree,
            'price': self.price,
            'category': self.category.to_json(),
            'authors': self.get_authors()
        }

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Author(models.Model):
    name = models.CharField(max_length=255)
    bookCount = models.IntegerField(default=0)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'bookCount': self.bookCount,
        }

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Authormap(models.Model):
    bookId = models.IntegerField()
    authorId = models.IntegerField()

    def __str__(self):
        return f"ID: {self.id}"

    def to_json(self):
        return {
            'id': self.id,
            'bookId': self.bookId,
            'authorId': self.authorId,
        }

    class Meta:
        verbose_name = "Authormap"
        verbose_name_plural = "Authormaps"
