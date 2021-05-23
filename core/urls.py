from django.urls import path
from .views import index, product, contact

urlpatterns = [
  path('', index),
  path('product', product),
  path('contact', contact)
]