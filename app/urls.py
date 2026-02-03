from django.contrib import admin
from django.urls import path
from books.views import book_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book_view, name='book-list'),
]
