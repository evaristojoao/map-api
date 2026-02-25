from django.db.models import Avg
from rest_framework import serializers
from categories.serializers import CategorySerializer
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Book
        fields = '__all__'


class BookListDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        return None

    class Meta:
        model = Book
        fields = ['id', 'title', 'city', 'description', 'travel_days', 'categories', 'language', 'rate']
