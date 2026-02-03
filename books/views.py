import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from books.models import Book


@csrf_exempt
def book_view(request):
    if request.method == 'GET':
        books = Book.objects.all()
        data = [{'id': book.id, 'name': book.name} for book in books]

        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        # padrão caracteres para não quebrar a string inputada
        data = json.loads(request.body.decode('utf-8'))

        new_book = Book(name=data['name'])
        new_book.save()

        return JsonResponse({'id': new_book.id, 'name': new_book.name}, status=201)
