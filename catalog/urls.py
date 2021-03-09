from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'categorys', CategoryViewSet)
router.register(r'colors', ColorViewSet)
router.register(r'products', ProductsViewSet)

urlpatterns = [
  path('', include(router.urls)),
]