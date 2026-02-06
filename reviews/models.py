from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from books.models import Book


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'The review cannot be lower than 0 stars.'),
            MaxValueValidator(5, 'The review cannot be higher than 5 stars.')
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.book
