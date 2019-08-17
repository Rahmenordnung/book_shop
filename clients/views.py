from django.shortcuts import render
from shopping_list.models import Order


def profile_view(request):
  orders = Order.objects.filter(user=request.user, item_checked=True)
  context = {
    'orders': orders
  }
  return render(request, "profile.html", context )
