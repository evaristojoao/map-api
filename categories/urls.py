from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryCreateListView.as_view(),
         name='category-create-list'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(),
         name='category-detail-view'),
]
