from django.urls import path
from .views import index, product, contact

urlpatterns = [
  path('', index),
  path('product', product, name='product'),
  path('contact', contact, name='contact')
]