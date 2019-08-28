from django.contrib import admin
from .models import Order, OrderItem, money_payment


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(money_payment)
