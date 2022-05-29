from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    another = models.CharField(max_length=100, null=True)
    is_best_seller = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("book_page", args=[self.id])

    def __str__(self):
        return f'{self.title} - ({self.rating})'
