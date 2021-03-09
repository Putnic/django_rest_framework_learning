from django.db import models


class Category(models.Model):
  name = models.CharField('Название', max_length=50)
  guid = models.CharField('Внешний ID', max_length=100, unique=True)
  parent = models.CharField('Родитель', max_length=100, blank=True)

  def __str__(self):
    return f'{self.guid} - {self.name}'

  class Meta:
    verbose_name = 'Категории и подкатегории'


class Color(models.Model):
  name = models.CharField('Название', max_length=50, unique=True)
  guid = models.CharField('Внешний ID', max_length=100, unique=True)
  hexcode = models.CharField('hex-код', max_length=100, unique=True)

  def __str__(self):
    return f'{self.guid} - {self.name}'

  class Meta:
    verbose_name = 'Цвета'


class Products(models.Model):
  name = models.CharField('Название', max_length=50)
  guid = models.CharField('Внешний ID', max_length=100, unique=True)
  color = models.ForeignKey('Color', on_delete=models.CASCADE)
  category = models.ForeignKey(
      'Category', on_delete=models.CASCADE, related_name='products')
  price = models.DecimalField(
      'Цена', max_length=100, null=True, max_digits=10, decimal_places=2)

  def __str__(self):
    return f'{self.guid} - {self.name}'

  class Meta:
    verbose_name = 'Товары'
