from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from books.models import Book
from books.serializers import BookSerializer
from reviews.models import Review


class BookCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,) # defino as permissões
    queryset = Book.objects.all()

    def get(self, request): # Action é o metodo GET
        total_books = self.queryset.count()
        books_by_categories = self.queryset.values('categories__name').annotate(count=Count('id')) # esta query traz o nome da categoria e a quantidade de categorias que tem
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(data={
            'total_books': total_books,
            'books_by_categories': books_by_categories,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0, # recebo round average_stars caso exista average stars, senao recebo zero
        },
        status=status.HTTP_200_OK)


