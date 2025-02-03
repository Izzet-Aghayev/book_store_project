from re import L
from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)

from core.utils.models import TrackingModel


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'



class Book(TrackingModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    offer_price  = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], null=True, blank=True)
    offer_dedline = models.DateTimeField()  # 2025-02-16 13:00
    number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
    book_isbn = models.CharField(unique=True, max_length=13, validators=[MinLengthValidator(13)])
    description = models.TextField(null=True, blank=True)
    book_image = models.ImageField(upload_to='book_media/')



class BuyBookNumber(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    
    def __str__(self):
        return self.book