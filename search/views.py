from django.db.models import Q
from django.shortcuts import render
from literature.models import Work, Category

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
  category = request.GET.get('category')
  reviewed = request.GET.get('reviewed')
  not_reviewed = request.GET.get('notReviewed')
  
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
  
  if is_valid_search_queryparam(category) and category != 'Choose...':
        qs = qs.filter(categories__name=category)
        
  if reviewed == 'on':
        qs = qs.filter(reviewed=True)

  elif not_reviewed == 'on':
        qs = qs.filter(reviewed=False)              
        
  context = {
    'queryset': qs,
    'categories': categories
      
  }  
  return render(request, "search_form.html", context)



def search_function(request):
  literature_work = Work.objects.filter(name_icontains=request.GET['q'])
  return render(request, "works_list.html", {"literature_work":literature_work})
