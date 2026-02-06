from django.contrib import admin
from django.urls import path
from books.views import BookCreateListView, BookRetrieveUpdateDestroyView
from categories.views import CategoryCreateListView, CategoryRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('books/', BookCreateListView.as_view(), name='book-create-list'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail-view'),
    
    path('categories/', CategoryCreateListView.as_view(), name='category-create-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail-view'),

    path('reviews/', ReviewCreateListView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
]
