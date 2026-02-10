from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name")

    class Meta:
        model = Book
        fields = '__all__'
