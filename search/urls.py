from django.urls import path
from search.views import search_formularView, search_function

app_name = 'search'

urlpatterns = [
  path('search/search_formularView/', search_formularView, name='formular'),
  path('', search_function, name='search')
  
  # url(r'^$', search_function, name='search')
]