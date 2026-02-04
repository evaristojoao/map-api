from django.contrib import admin
from django.urls import path
from books.views import BookCreateListView, BookRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookCreateListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail-view'),
]
