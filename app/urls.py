from django.contrib import admin
from django.urls import path
from books.views import book_create_list_view, book_detail_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book_create_list_view, name='book-list'),
    path('books/<int:pk>/', book_detail_view, name='book-detail-view'),
]
