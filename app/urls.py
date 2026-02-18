from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/v1/', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path('api/v1/', include('categories.urls')),
    path('api/v1/', include('reviews.urls')),
]
