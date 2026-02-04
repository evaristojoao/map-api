import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from books.models import Book


@csrf_exempt 
def book_create_list_view(request):
    if request.method == 'GET':
        books = Book.objects.all()
        data = [{'id': book.id, 'name': book.name} for book in books]

        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        new_book = Book(name=data['name'])
        new_book.save()

        return JsonResponse({'id': new_book.id, 'name': new_book.name}, status=201)


@csrf_exempt 
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'GET':
        data = {'id': book.id, 'name': book.name}

        return JsonResponse(data)
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        book.name = data['name']
        book.save()

        return JsonResponse({'id': book.id, 'name': book.name}, status=201)
