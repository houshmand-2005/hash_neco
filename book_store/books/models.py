import code
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal_code}"

    class Meta:
        verbose_name_plural = ("Addresses Entries")


class Another(models.Model):  # Author
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        "Address",  on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    another = models.ForeignKey(
        Another, on_delete=models.CASCADE, null=True, related_name="books")
    is_best_seller = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False,
                            db_index=True, blank=True)
    publish_country = models.ManyToManyField(Country)
    def get_absolute_url(self):
        return reverse("book_page", args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - ({self.rating})'
