from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookCreateListView.as_view(), name='book-create-list'),
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view(),
         name='book-detail-view'),
    path('books/stats/', views.BookStatsView.as_view(), name='book-stats-view'),
]
