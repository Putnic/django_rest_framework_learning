from rest_framework import serializers
from .models import Products, Category, Color


class CategorySerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Category
    fields = ['id', 'url', 'name', 'guid', 'parent', 'products']


class ColorSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Color
    fields = ['id', 'url', 'name', 'guid', 'hexcode']


class ProductsSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Products
    fields = ['id', 'url', 'name', 'guid', 'category', 'color', 'price']