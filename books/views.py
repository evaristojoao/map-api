from django.http import JsonResponse
from books.models import Book


def book_view(request):
    books = Book.objects.all() 
    data = [{ 'id': book.id, 'name': book.name} for book in books] 
    return JsonResponse(data, safe=False) 
