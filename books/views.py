import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from books.models import Book
from rest_framework import generics
from books.serializers import BookSerializer


class BookCreateListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

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
    elif request.method == 'DELETE':
        book.delete()

        return JsonResponse({'message': 'Book deleted with success.'}, status=204)
