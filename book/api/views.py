from django.http.response import JsonResponse

from api.models import Category, Book, Author, Authormap


def category_list(request):
    items = Category.objects.all()
    items_json = [item.to_json() for item in items]
    return JsonResponse(items_json, safe=False)


def book_list(request):
    items = Book.objects.all()
    items_json = [item.to_json() for item in items]
    return JsonResponse(items_json, safe=False)


def book(request, pk=None):
    try:
        item = Book.objects.get(id=pk)
        return JsonResponse(item.to_json())
    except Book.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
        })


def author_list(request):
    items = Author.objects.all()
    items_json = [item.to_json() for item in items]
    return JsonResponse(items_json, safe=False)


def authormap_list(request):
    items = Authormap.objects.all()
    items_json = [item.to_json() for item in items]
    return JsonResponse(items_json, safe=False)
