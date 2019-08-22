from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from literature.models import Work
from .models import Order, OrderItem, money_payment
import stripe
import random
import string

stripe.api_key = settings.STRIPE_SECRET

def create_ref_code():
  return ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
  
@login_required
def add_to_cart(request, work_slug):
  work = get_object_or_404(Work, slug=work_slug)
  order_item, created = OrderItem.objects.get_or_create(work=work)
  order, created = Order.objects.get_or_create(
      user=request.user, item_checked=False)
  order.items.add(order_item)
  order.save()
  messages.info(request, "Literary work successfully added to your cart.")
  return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def remove_from_cart(request, work_slug):
  work = get_object_or_404 (Work, slug=work_slug)
  order_item = get_object_or_404 (OrderItem, work=work)
  order = Order.objects.get (user=request.user, item_checked=False)
  order.items.remove(order_item)
  order.save()
  messages.info(request, "Literary work successfully removed to your cart.")
  return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def order_view(request):
  order_qs = Order.objects.filter (user=request.user, item_checked=False)
  if order_qs.exists():
    context = {
      'order': order_qs[0]
    }
    return render(request, "complete_order_list.html", context)
  return Http404

@login_required
def checkout(request):
    order_qs = Order.objects.filter(user=request.user, item_checked=False)
    if order_qs.exists():
        order = order_qs[0]
    else:
        return Http404
    if request.method == "POST":
        try:
            # complete the order (ref code and set ordered to true)
            order.ref_code = create_ref_code()

            # create a stripe charge
            token = request.POST.get('stripeToken')
            charge = stripe.Charge.create(
                amount=int(order.get_total() * 100),  # cents
                currency="usd",
                source=token,  # obtained with Stripe.js
                description=f"Charge for {request.user.username}"
            )

            # create our payment object and link to the order
            payment = money_payment()
            payment.order = order
            payment.stipe_charge_id = charge.id
            payment.total_amount = order.get_total()
            payment.save()

            # add the book to the users book list
            works = [item.work for item in order.items.all()]
            for work in works:
              request.user.userlibrary.works_owned.add(work)

            order.item_checked = True
            order.save()

            # redirect to the users profile
            messages.success(request, "Your order is now being processed!")
            return redirect("/account/profile/")

        # send email to yourself

        except stripe.error.CardError as e:
            messages.error(request, "There was a error with the card.")
            return redirect(reverse("cart:checkout"))
        except stripe.error.RateLimitError as e:
            messages.error(request, "There was a rate limit error on Stripe.")
            return redirect(reverse("cart:checkout"))
        except stripe.error.InvalidRequestError as e:
            messages.error(request, "The introduced data is invalid for Stripe request.")
            return redirect(reverse("cart:checkout"))
        except stripe.error.AuthenticationError as e:
            messages.error(request, "Invalid Stripe API keys.")
            return redirect(reverse("cart:checkout"))
        except stripe.error.APIConnectionError as e:
            messages.error(
                request, "There was a network error. Please try again.")
            return redirect(reverse("cart:checkout"))
        except stripe.error.StripeError as e:
            messages.error(request, "There was an error. Please try again.")
            return redirect(reverse("cart:checkout"))
        except Exception as e:
            messages.error(
                request, "System issue. We are working to resolve the issue.")
            return redirect(reverse("cart:checkout"))

    context = {
        'order': order
    }

    return render(request, "checkout.html", context)