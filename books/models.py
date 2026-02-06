from django.db import models
from django.utils.text import slugify
from categories.models import Category


class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, blank=True)
    city = models.CharField(max_length=100, db_index=True)
    travel_days = models.PositiveIntegerField(blank=True, null=True)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    file_url = models.URLField(blank=True, null=True)
    cover_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=3, default="pt")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='books', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
