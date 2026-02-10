from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(
        read_only=True,
        slug_field="title"
    )

    class Meta:
        model = Review
        fields = '__all__'
