from django.shortcuts import render
from literature.models import Work

def search_function(request):
  literature_work = Work.objects.filter(name_icontains=request.GET['q'])
  return render(request, "works_list.html", {"literature_work":literature_work}) 
