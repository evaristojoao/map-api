from rest_framework import serializers
from books.models import Book
from reviews.serializers import ReviewSerializer


class BookSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    def get_rate(self, obj):
        reviews = obj.reviews.all()

        if reviews:
            sum_reviews = 0

            for review in reviews:
                sum_reviews += review.stars

            reviews_count = reviews.count()

            return round(sum_reviews / reviews_count, 1)

        return None
