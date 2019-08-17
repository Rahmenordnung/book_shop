from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Work, Part, Text
from shopping_list.models import Order, OrderItem

OWNED = 'owned'
IN_CART_CHECK = 'in_cart_check' 
NOT_IN_CART_CHECK = 'not_in_cart_check'

def works_relate_property(request, work):
    if work in request.user.userlibrary.work_list():
        return OWNED
    order_qs = Order.objects.filter(user=request.user, item_checked=False)
    if order_qs.exists():
        order = order_qs[0]
        order_item_qs = OrderItem.objects.filter(work=work)
        if order_item_qs.exists():
            order_item = order_item_qs[0]
            if order_item in order.items.all():
                return IN_CART_CHECK
    return NOT_IN_CART_CHECK   
        
def works_list(request):
  # display all of the theater_work
  queryset = Work.objects.all()         
  context = {
    'queryset': queryset
  }
  return render(request, "works_list.html", context)

def work_detail(request, slug):
  # display some details of the work presented
  work = get_object_or_404(Work, slug=slug)
  work_status = works_relate_property(request, work)
  context = {
    'work': work,
    'work_status': work_status
  }
  return render(request, "work_detail.html", context)

def part_detail(request, work_slug, part_number):
  part_qs = Part.objects \
    .filter(work__slug=work_slug) \
    .filter(part_number=part_number)
  part = part_qs[0]
  work_status = works_relate_property(request, part.work)
  if part_qs.exists():
    context = {
      'part': part,
      'work_status': work_status 
    }
    return render(request, "part_detail.html", context)
  return Http404

def text_detail(request, work_slug, part_number, text_number):
  text_qs = Text.objects \
    .filter(part__work__slug=work_slug) \
    .filter(part__part_number=part_number) \
    .filter(text_number = text_number)
  text = text_qs[0]  
  work_status = works_relate_property(request, text.part.work)  
  if text_qs.exists():
    context = {
      'text': text,
      'work_status': work_status 
    }
    return render(request, "text_detail.html", context)
  return Http404                 
                
