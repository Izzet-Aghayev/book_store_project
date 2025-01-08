from django.db import models

from core.utils.models import TrackingModel


class CategoryModel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class BooksModel(TrackingModel, models.Model):
    categories = models.ManyToManyField(CategoryModel)

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_dedline = models.DateTimeField()
    number = models.IntegerField()
    description = models.TextField(null=True, blank=True)