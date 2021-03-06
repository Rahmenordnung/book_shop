from django.urls import path
from .views import works_list, work_detail, part_detail, text_detail #SearchResultsView #results#, 

app_name = 'literature'

urlpatterns = [
  path('',works_list, name='works_list'),
  # path('search/', SearchResultsView.as_view(), name='search_results'),
  # path('search/results/',results, name='results'),
  path('<slug>/', work_detail, name='work_detail'),
  path('<work_slug>/<int:part_number>', part_detail, name='part-detail'),
  path('<work_slug>/<int:part_number>/<int:text_number>/', text_detail, name='text_detail'),

]