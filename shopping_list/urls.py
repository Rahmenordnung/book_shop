from django.urls import path
from .views import (add_to_cart, remove_from_cart, order_view, checkout)

app_name = "shopping_list"

urlpatterns = [
  path('add-to-cart/<work_slug>/', add_to_cart,name='add-to-cart'),
  path('remove-from-cart/<work_slug>/', remove_from_cart,name='remove-from-cart'),
  path('complete_order_list/', order_view, name='complete_order_list'),
  path('checkout/', checkout, name='checkout'),
]
