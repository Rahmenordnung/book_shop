from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from literature.models import Work
from .models import Order, OrderItem, money_payment
import stripe
import random
import string

stripe.api_key = settings.STRIPE_SECRET

def create_ref_code():
  ''+join(random.choices(string.ascii_uppercase + string.digits, k=15))
  

def add_to_cart(request, work_slug):
  work = get_object_or_404(Work, slug=work_slug)
  order_item, created = OrderItem.objects.get_or_create(work=work)
  order, created = Order.objects.get_or_create(
      user=request.user, item_checked=False)
  order.items.add(order_item)
  order.save()
  # messages.info(request, "Item successfully added to your cart.")
  return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def remove_from_cart(request, work_slug):
  work = get_object_or_404 (Work, slug=work_slug)
  order_item = get_object_or_404 (OrderItem, work=work)
  order = get_object_or_404 (Order, user=request.user)
  order.items.remove(order_item)
  order.save()
  return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def order_view(request):
  order = get_object_or_404 (Order, user=request.user)
  context = {
    'order': order
  }
  return render(request, "complete_order_list.html", context)

def checkout(request):
  order = get_object_or_404 (Order, user=request.user)
  if request.method == "POST":
  # complete the order (ref code and item_checked to true)
    
    order.ref_code = create_ref_code()
    
  # create a stripe charge
    charge = stripe.Charge.create(
      amount=order.get_total() * 100, #cents
      curency="eur",
      source="tok_amex", # obtained with Stripe.js
      description= f"Charge for {request.user.username}"
    )
  
  # create the moneypayment and connect it to the order
    
    money_payment = Payment()
    money_payment.order = order
    money_payment.stripe_charge_id = charge.id 
    money_payment.total_amount = order.get_total()
    money_payment.save()

    # add the work to the users worl list
    works = [item.work for item in order.items.all()]
    for work in works:
      request.user.userlibrary.items.add()
    
  
  # redirect to the user profile
    return redirect("/account/profile/")
  
  context = {
        'order': order
    }

  return render(request, "checkout.html", context)