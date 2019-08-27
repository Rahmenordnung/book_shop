from django.db.models import Q
from django.shortcuts import render
from literature.models import Work, Category 
# from django.shortcuts import render, get_object_or_404
# Category

def is_valid_search_queryparam(param):
  return param != '' and param is not None

def search_formularView(request):
  qs = Work.objects.all() 
  categories = Category.objects.all() 
#  display all of the literary_work
  
  title_contains_query = request.GET.get('title_contains')
  work_price_query = request.GET.get('work_price')
  maestros_or_title_query = request.GET.get('maestros_or_title')
  view_count_min = request.GET.get('view_count_min')
  view_count_max = request.GET.get('view_count_max')
  date_min = request.GET.get('date_min')
  date_max = request.GET.get('date_max')
  bestseller = request.GET.get('bestseller')
  not_bestseller = request.GET.get('notbestseller')
  is_longbook = request.GET.get('longbook')
  is_shortbook = request.GET.get('isshortbook')
  worldwide_appreciated = request.GET.get('worldwide_appreciated')
  underground_appreciation = request.GET.get('underground_appreciation')
  
  if is_valid_search_queryparam(title_contains_query):
    qs = qs.filter(title__icontains=title_contains_query)
  elif is_valid_search_queryparam(work_price_query):
    qs = qs.filter(price__iexact=work_price_query)
  elif is_valid_search_queryparam(maestros_or_title_query):
    qs = qs.filter(Q(title__icontains=maestros_or_title_query)
                       | Q(maestros__completename__icontains=maestros_or_title_query)
                       ).distinct()
    
  if is_valid_search_queryparam(view_count_min):
        qs = qs.filter(views__gte=view_count_min)

  if is_valid_search_queryparam(view_count_max):
        qs = qs.filter(views__lt=view_count_max)

  if is_valid_search_queryparam(date_min):
        qs = qs.filter(publication_date__gte=date_min)

  if is_valid_search_queryparam(date_max):
        qs = qs.filter(publication_date__lt=date_max)
  
  # if is_valid_search_queryparam(category) and category != 'Choose...':
  #       qs = qs.filter(categories__name=category)
        
  if bestseller == 'on':
        qs = qs.filter(bestseller=True)

  elif not_bestseller == 'on':
        qs = qs.filter(bestseller=False) 
        
  if is_longbook == 'on':
        qs = qs.filter(longbook=True)

  elif is_shortbook == 'on':
        qs = qs.filter(longbook=False)
  
  if worldwide_appreciated == 'on':
        qs = qs.filter(worldwide_appreciated=True)

  elif underground_appreciation == 'on':
        qs = qs.filter(worldwide_appreciated=False)                          
        
  context = {
    'queryset': qs,
    'categories': categories
      
  }  
  return render(request, "search_form.html", context)

# def get_products_by_category(request, category):
#     category_we_are_retrieving = get_object_or_404(Category, type=category)
#     products = Work.objects.filter(category = category_we_are_retrieving)
#     return render(request, 'search_form.html', {'products': products, 'title': 'Browse all {}'.format(category_we_are_retrieving.type)})

def search_function(request):
  literature_work = Work.objects.filter(name_icontains=request.GET['q'])
  return render(request, "works_list.html", {"literature_work":literature_work})