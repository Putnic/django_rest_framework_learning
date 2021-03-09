from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, ColorSerializer, ProductsSerializer
from .models import Products, Category, Color
from .tasks import add


class CategoryViewSet(viewsets.ModelViewSet):
  '''
  API endpoint Category
  '''
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class ColorViewSet(viewsets.ModelViewSet):
  '''
  API endpoint Color
  '''
  queryset = Color.objects.all()
  serializer_class = ColorSerializer


class ProductsViewSet(viewsets.ModelViewSet):
  '''
  API endpoint Products
  '''
  queryset = Products.objects.all()
  serializer_class = ProductsSerializer
