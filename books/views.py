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
    if request.method == 'GET':
        book = get_object_or_404(Book, pk=pk)
        data = {'id': book.id, 'name': book.name}

        return JsonResponse(data)


