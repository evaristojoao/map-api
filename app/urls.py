from django.contrib import admin
from django.urls import path
from books.views import BookCreateListView, book_detail_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookCreateListView.as_view(), name='book-list'),
    path('books/<int:pk>/', book_detail_view, name='book-detail-view'),
]
