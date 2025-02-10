from rest_framework import serializers

from ..models import (
    Category,
    Book,
    BuyBookNumber
)



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields  = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BuyBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyBookNumber
        fields = ('number',)