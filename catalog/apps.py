from django.apps import AppConfig
from django.db.models.signals import class_prepared
import os
from .signals import init_model


class CatalogConfig(AppConfig):
  name = 'catalog'

  def ready(self):
    super().ready()
    print('***** catalog apps PID *****', os.getpid())
    from .models import Category, Color, Products
    if Category.objects.exists() or Color.objects.exists() or Products.objects.exists():
      class_prepared.disconnect()
    else:
      class_prepared.connect(init_model)
