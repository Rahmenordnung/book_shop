from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Work, Part, Text, Maestro
from shopping_list.models import Order, OrderItem
from django.views.generic import TemplateView, ListView
from .models import Work
# from django.core.paginator import Paginator


# class WorksPageView(TemplateView):
#     template_name = 'works_list.html'

# # class SearchResultsView(ListView):
# #     model = Work
# #     template_name = 'search_results.html'
# #     def get_queryset(self): # new
# #         query = self.request.GET.get('q')
# #         object_list = Work.objects.filter(
# #             Q(title__icontains=query) | Q(price__icontains=query)
# #         )
# #         return object_list


OWNED = 'owned'
IN_CART_CHECK = 'in_cart_check' 
NOT_IN_CART_CHECK = 'not_in_cart_check'

# def search(request):        
#     if request.method == 'POST':      
#         book_name =  request.POST.getlist('search')      
#         try:
#             status = Work.objects.filter(work__icontains=title)
#             #Add_prod class contains a column called 'bookname'
#         except Work.DoesNotExist:
#             status = None
#         return render(request,"search.html",{"works":status})
#     else:
#         return render(request,"search.html",{})

# def results(request):    
#   search_text = request.GET.get('q','results')    
#   results = Work.objects.filter(title__icontains=search_text)    
#   return results  # via render_to_response, of course

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
  qs = Work.objects.all()
  title_contains_query = request.GET.get('title_contains')
  if title_contains_query != '' and title_contains_query is not None:
    qs = qs.filter(title__icontains=title_contains_query)  
 # display all of the literary_work
  context = {
    'queryset': qs  
  }
  # query_items = request.GET. get("q")
  
  # paginator = Paginator(Work, 1)
  # page = request.GET.get('page')
  # context = paginator.get_page(page)
  
  # if query_items: 
  #   queryset_list = queryset_list.filter(Work.title__icontains=queryset_list)
    
  return render(request, "works_list.html", context)

@login_required
def work_detail(request, slug):
  # display some details of the work presented
  work = get_object_or_404(Work, slug=slug)
  work_status = works_relate_property(request, work)
  context = {
    'work': work,
    'work_status': work_status
  }
  return render(request, "work_detail.html", context)

@login_required
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

@login_required
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
                
