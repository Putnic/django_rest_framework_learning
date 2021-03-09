from __future__ import absolute_import, unicode_literals
import os


def init_model(sender, **kwargs):
  from .tasks import init_data

  BASE_DIR = os.path.dirname(os.path.abspath(__file__))
  file_json = os.path.join(BASE_DIR, './fixtures/data.json')
  init_data.delay(file_json)