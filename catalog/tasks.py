# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import json

from urllib.parse import unquote
from .models import Category, Color, Products


@shared_task
def init_data(file):
  models = {'сategory': Category, 'Color': Color, 'Products': Products}

  with open(file, 'r', encoding='utf-8') as f:
    data_str = unquote(f.read())
    data_obj = json.loads(data_str, encoding='utf-8')

  for model in data_obj['models']:
    model_obj = models[model['model']]

    if model_obj.objects.exists():
      continue

    if model['model'] != 'Products':
      for item in model['items']:
        model_obj.objects.create(**item)
    else:
      for item in model['items']:
        item['category'] = Category.objects.get(guid=item['category'])
        item['color'] = Color.objects.get(guid=item['color'])
        model_obj.objects.create(**item)
